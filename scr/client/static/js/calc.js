$(document).ready(function() {
  // Обработчик клика по кнопке "Рассчитать"
  $('#js-button').click(function() {
    var size = $('#size').val(); // Значение выбранного диаметра колеса
    var quantity = $('#quantity').val(); // Значение выбранного количества шин
    var period = $('#period').val(); // Значение выбранного срока хранения

    // Ваш код для расчета стоимости на основе выбранных параметров
    // Пример расчета стоимости: (просто для иллюстрации)
    var cost = parseInt(size) * parseInt(quantity) * parseInt(period);

    // Обновление отображения стоимости
    $('#summ').text(cost + ' руб');
  });
});
