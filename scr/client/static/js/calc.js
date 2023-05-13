$(document).ready(function(){
    $("#kolvo").keydown(function(event) {
        // Разрешаем: backspace, delete, tab и escape
        if ( event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 ||
             // Разрешаем: Ctrl+A
            (event.keyCode == 65 && event.ctrlKey === true) ||
             // Разрешаем: home, end, влево, вправо
            (event.keyCode >= 35 && event.keyCode <= 39)) {
                 // Ничего не делаем
                 return;
        }
        else {
            // Обеждаемся, что это цифра, и останавливаем событие keypress
            if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                event.preventDefault();
            }
        }
    });

    $('#js-button').click(function(){

        var value1 = $('#size').val();
        var value2 = $('#period').val();
        var value3 = $('#quantity').val();
        if (value2 > 30) {
            $('#summ').html("Стоимость услуги"+ "&nbsp;" + " " + value1*value2*value3/1.5 + " ₽");
          } else {
            $('#summ').html("Стоимость услуги"+ "&nbsp;" + " " + value1*value2*value3 + " ₽");
          }
        // $('#summ').html("Стоимость услуги"+ "&nbsp;" + " " + value1*value2*value3 + " ₽");
    });
});