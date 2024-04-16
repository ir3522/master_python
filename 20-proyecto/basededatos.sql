CREATE DATABASE IF NOT EXISTS python;
USE python;

CREATE TABLE usuarios (
  id INT NOT NULL AUTO_INCREMENT,  -- Unique identifier (primary key)
  nombre VARCHAR(100) NOT NULL,    -- User's first name
  apellidos VARCHAR(255) NOT NULL,  -- User's last name
  email VARCHAR(255) NOT NULL UNIQUE,  -- User's email (unique constraint)
  password VARCHAR(255) NOT NULL,    -- User's password (hashed)
  fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- Registration date and time
  CONSTRAINT pk_usuarios PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE notas (
  id INT NOT NULL AUTO_INCREMENT,  -- Unique note identifier
  usuario_id INT NOT NULL,    -- Foreign key to usuarios table
  titulo VARCHAR(255) NOT NULL,  -- Note title
  descripcion MEDIUMTEXT,      -- Note description
  fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- Note creation date and time
  CONSTRAINT pk_notas PRIMARY KEY (id),
  CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
) ENGINE=InnoDB;