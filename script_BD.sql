-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS biblioteca_db;
USE biblioteca_db;

-- Tabla de libros
CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    anio_publicacion INT NOT NULL
);


-- Insertar datos de ejemplo
INSERT INTO libros (titulo, autor, anio_publicacion) VALUES 
('cien años de soledad', 'Gabriela Garcia Marquez', 1967),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605),
('1984', 'George Orwell', 1949),
("Rayuela", "Julio Cortazar", 1963),
("El principito", "Antoine de Saint-Exupery", 1943)
