Feature: Cambiar foto del grupo
  Como usuario perteneciente a un grupo
  Quiero cambiar la foto del grupo
  Para poder actualizarlo

  Scenario: Cambiar foto siendo administrador
    Given soy administrador del grupo
    When subo una nueva foto para el grupo
    Then la foto del grupo se actualiza correctamente

  Scenario: Cambiar foto sin ser administrador
    Given no soy administrador del grupo
    When intento cambiar la foto del grupo
    Then no puedo cambiarla y me avisa que no tengo permisos.