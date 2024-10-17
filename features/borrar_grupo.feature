Feature: Borrar grupo
  Como usuario perteneciente a un grupo
  Quiero borrar el grupo
  Para no tener grupos que ya no utilizamos

  Scenario: Borrar grupo siendo administrador
    Given soy administrador del grupo
    When selecciono la opción de borrar el grupo
    Then el grupo se elimina permanentemente y no está disponible en la lista de grupos.

  Scenario: Borrar grupo sin ser administrador
    Given no soy administrador del grupo
    When intento borrar el grupo
    Then no puedo borrarlo y me avisa que no tengo permisos.