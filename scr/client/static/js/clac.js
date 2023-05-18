$(document).ready(function() {
  // Функция для обновления стоимости
  function updateCost() {
    var size = $('#id_size option:selected').text();
    var quantity = $('#id_quantity option:selected').text();
    var period = $('#id_period option:selected').text();
    var address = $('#id_adress option:selected').text();

    // Ваш код для расчета стоимости на основе выбранных параметров
    // Пример расчета стоимости: (просто для иллюстрации)
    var cost = parseInt(size) * parseInt(quantity) * parseInt(period);

    // Обновление отображения стоимости
    $('#summ').text(cost + ' руб');
  }

  // Обработчики событий для каждого select
  $('#id_size').change(function() {
    updateCost();
  });

  $('#id_quantity').change(function() {
    updateCost();
  });

  $('#id_period').change(function() {
    updateCost();
  });

  $('#id_adress').change(function() {
    updateCost();
  });
});
