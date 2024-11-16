from sqlalchemy import create_engine, text, select
from sqlalchemy import String, ForeignKey
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship, DeclarativeBase
from typing import Optional, List


# -- UTILIZANDO EXPRESIONES TEXTUALES SIN ORM (CORE) --
def sql_core(motor: Engine):
    # Conectarse con connect()
    with motor.connect() as conn:  # Realiza un rollback al finalizar
        res = conn.execute(text('SELECT "Hola mundo"'))
        print(res.all())

    with motor.begin() as conn:  # Realiza un commit al finalizar
        conn.execute(text('CREATE TABLE IF NOT EXISTS ejemplo (x int, y int)'))
        conn.execute(
            text('INSERT INTO ejemplo (x, y) VALUES (:x, :y)'),
            # Se pueden insertar varios valores utilizando diccionarios
            ({'x': 1, 'y': 1}, {'x': 2, 'y': 2})
        )

    with motor.connect() as conn:
        res = conn.execute(text('SELECT * FROM ejemplo'))
        # El resultado es un NamedTuple con el nombre de la columna. Podemos recorrerlo de la siguiente manera
        for x, y in res:
            print(f'X = {x}, Y = {y}')
        # Segun su indice
        res = conn.execute(text('SELECT * FROM ejemplo'))
        for fila in res:
            print(f'X = {fila[0]}, Y = {fila[1]}')
        # Segun el atributo
        res = conn.execute(text('SELECT * FROM ejemplo'))
        for fila in res:
            print(f'X = {fila.x}, Y = {fila.y}')
        # Segun mapeo con MAPPINGS()
        res = conn.execute(text('SELECT * FROM ejemplo'))
        for dict_fila in res.mappings():
            print(f'X = {dict_fila['x']}, Y = {dict_fila['y']}')


# -- UTILIZANDO ORM --
def sql_orm(motor: Engine):
    # Conectarse con Session()
    query = text("SELECT x, y FROM ejemplo WHERE y > :y ORDER BY x, y")
    with Session(motor) as sesion:
        res = sesion.execute(query, {'y': 6})
        for row in res:
            print(f"x: {row.x}  y: {row.y}")


def insert_orm(motor: Engine):
    """Funcion para insertar nuevos datos a una tabla a traves de una Session"""
    calamardo = Usuario(nombre='calamardo', nombre_completo='Calamardo')
    don_cangrejo = Usuario(nombre='cangrejo', nombre_completo='Don Cangrejo')
    print(calamardo)  # __repr__ de Usuario
    sesion = Session(motor)
    # Anadir objetos a la sesion
    sesion.add(calamardo)
    sesion.add(don_cangrejo)
    # Ver que objetos han sido anadidos
    print(sesion.new)  # IdentitySet con los objetos a anadir
    sesion.commit()
    # Obtener el usuario recien agregado
    calamar = sesion.get(Usuario, 1)
    # Tanto el usuario anteriormente creado como el obtenido a traves de .get()
    # comparten espacio en memoria, por ende
    print(calamar is calamardo)  # True
    # Ya podemos obtener las nuevas primary keys de los objetos
    # utilizando el atributo "id"
    print(f'Primary keys: Calamardo={calamardo.id}, Don cangrejo={don_cangrejo.id}')


def select_orm(motor: Engine):
    """La funcion de seleccion es la misma tanto para ORM como Core.
    Solo varia la conexion"""
    with Session(motor) as sesion:
        calamardo = sesion.execute(select(Usuario).filter_by(nombre='calamardo')).scalar_one()
        print(calamardo)


def update_orm(motor: Engine):
    """Funcion para modificar datos en una tabla a traves de una sesion"""
    with Session(motor) as sesion:
        calamardo = sesion.execute(select(Usuario).filter_by(nombre='calamardo')).scalar_one()
        # Se puede actualizar un registro modificando sus atributos
        calamardo.nombre_completo = 'Calamardo Tules'
        # El objeto aparece en sesion.dirty indicando que fue modificado
        print(calamardo in sesion.dirty)  # True
        # Al realizar un nuevo Select, se realiza un flush
        # pero los cambios aun no son subidos. Seguimos en
        # la transaccion
        nombre_calamar = sesion.execute(select(Usuario.nombre_completo).where(Usuario.id == 1)).scalar_one()
        print(nombre_calamar)  # Calamardo Tules
        print(calamardo in sesion.dirty)  # False
        # Para subir los cambios, basta con un simple commit
        sesion.commit()


def delete_orm(motor: Engine):
    """Funcion para eliminar un registro de una tabla"""
    # Esta vez sin context manager (with)
    sesion = Session(motor)
    calamardo = sesion.get(Usuario, 1)
    sesion.delete(calamardo)
    # Hasta que no se realice un flush, no se eliminara,
    # solo queda marcado
    sesion.commit()
    sesion.close()


def manipular_datos(motor: Engine):
    user1 = Usuario(nombre='Rami', nombre_completo='Ramiro Tules')
    # La direccion es una lista vacia
    print(user1.direcciones)  # []
    # Crear direccion
    direc1 = Direccion(direc_email='ramitules@1234.com')
    # Insertar en la lista de direcciones del usuario
    user1.direcciones.append(direc1)
    print(user1.direcciones)  # [Direccion(id=None, direc_email='ramitules@1234.com')]
    # Imprimir el usuario asociado a la direccion mediante 'relationship()'
    print(direc1.usuario)  # Usuario(id=None, nombre='Rami', nombre_completo='Ramiro Tules')
    # Tambien se puede asociar una direccion a un usuario
    # pasandole el usuario como argumento
    direc2 = Direccion(direc_email='ramitules@9876.com', usuario=user1)
    print(user1.direcciones)  # Lista con ambas direcciones
    # De esta forma se comprueba que tanto los usuarios
    # como las direcciones estan asociadas de forma bidireccional
    # en memoria
    with Session(motor) as sesion:
        sesion.add(user1)
        # Se anade tanto el usuario como las direcciones asociadas
        print(user1 in sesion, direc1 in sesion, direc2 in sesion)  # True True True
        # Pero aun no esta nada creado
        print(user1.id)  # None
        # Al subir los cambios, se crean el usuario y sus direcciones
        # de forma ordenada para que las direcciones se puedan
        # asociar a una PK de usuarios utilizando foraneas
        sesion.commit()
        # Acceder al nuevo ID del usuario
        print(user1.id)  # Esto implica un SELECT
        # Acceder a las direccion
        print(user1.direcciones)  # Esto implica un SELECT
        # No se realizaran nuevas consultas a la base de datos si
        # ya ha sido cargado en memoria
        print(user1.direcciones)  # Esto NO implica un SElECT
        print(direc1)  # Direccion(id=1, direc_email='ramitules@1234.com')


def joins():
    # Realizar un JOIN
    select(Direccion.direc_email).select_from(Usuario).join(Usuario.direcciones)
    # Realizar un JOIN utilizando "relationship()" de las clases creadas
    select(Direccion.direc_email).join_from(Usuario, Direccion)


class Base(DeclarativeBase):
    pass


class Usuario(Base):
    __tablename__ = 'usuarios'
    # Las anotaciones de tipo de datos (Mapped[]) son opcionales.
    # Sin anotaciones, mapped_column() deberia ser usado con los tipos
    # proporcionados por SQLAlchemy, como Integer o String
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30))
    nombre_completo: Mapped[Optional[str]]
    # Relacion uno a muchos
    # (Un usuario puede estar referenciado en varias direcciones)
    direcciones: Mapped[List["Direccion"]] = relationship(back_populates='usuario')

    def __repr__(self):
        return f'Usuario(id={self.id!r}, nombre={self.nombre!r}, nombre_completo={self.nombre_completo!r})'


class Direccion(Base):
    __tablename__ = 'direccion'

    id: Mapped[int] = mapped_column(primary_key=True)
    direc_email: Mapped[str]
    id_usuario = mapped_column(ForeignKey('usuarios.id'))
    # Relacion varios a uno
    # (Varias direcciones pueden estar asociadas a un usuario)
    usuario: Mapped[Usuario] = relationship(back_populates='direcciones')

    def __repr__(self):
        return f'Direccion(id={self.id!r}, direc_email={self.direc_email!r})'


if __name__ == '__main__':
    # Crear un motor. Esto deberia realizarse una sola vez por ejecucion,
    # por ende lo ideal es hacerlo global
    motor = create_engine(
        'sqlite+pysqlite:///ejemplo.db',  # Driver
        echo=True  # Log a stdout
    )
    # Despues de crear las tablas en Python, pueden subirse a la base de datos.
    # Omite la creacion si ya existe la tabla
    Base.metadata.create_all(motor)
    # De esta forma, creamos primero la clase Base,
    # luego las clases para cada una de las tablas,
    # y por ultimo creamos las tablas en la base de datos.
    '''insert_orm(motor)'''  # Insertar datos
    '''update_orm(motor)'''  # Actualizar datos
    '''delete_orm(motor)'''  # Eliminar datos
    # Manipular datos
    '''manipular_datos(motor)'''

