Feature: Registro de usuario
  Como potencial usuario de la aplicación
  Quiero poder registrarme
  Para poder crear grupos y eventos para dividir mis gastos

  Scenario: Registro con un email no existente
    Given no estoy registrado
    When me quiero registrar con un email que no existe previamente
    Then puedo ingresar la contraseña que deseo establecer

  Scenario: Registro con un email existente
    Given no estoy registrado
    When me quiero registrar con un email que ya existe previamente
    Then no puedo registrarme en la aplicación

  Scenario: Registro exitoso
    Given no estoy registrado
    When tengo un email válido e ingreso la contraseña deseada y la confirmo
    Then puedo registrar mi usuario y contraseña en la aplicación