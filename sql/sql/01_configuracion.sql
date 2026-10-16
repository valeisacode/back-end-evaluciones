
CREATE DATABASE IF NOT EXISTS control_tareas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'usuario_tareas'@'127.0.0.1'
IDENTIFIED BY 'Tareas_Local_2026!';

ALTER USER 'usuario_tareas'@'127.0.0.1'
IDENTIFIED BY 'Tareas_Local_2026!';

GRANT ALL PRIVILEGES ON control_tareas.*
TO 'usuario_tareas'@'127.0.0.1';