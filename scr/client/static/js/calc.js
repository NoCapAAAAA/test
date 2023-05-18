$(document).ready(function(){
    $('#js-button').click(function(){

        var size = $('#size').val();
        var period = $('#period').val();
        var quantity = $('#quantity').val();
        var period2 = period * 30
        if (period2 > 30) {
            $('#summ').html("Стоимость услуги"+ "&nbsp;" + " " + size*period*quantity/1.5 + " ₽");
          } else {
            $('#summ').html("Стоимость услуги"+ "&nbsp;" + " " + value1*value2*value3 + " ₽");
          }
        // $('#summ').html("Стоимость услуги"+ "&nbsp;" + " " + value1*value2*value3 + " ₽");
    });
});