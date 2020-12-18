
var headerWidth = $( window ).width();		// How wide the header is.

var id_jugador = "";

$(document).ready(function(){

    var arrowTime = setTimeout("mostrar('arrow_right')", 8000);

    if($('#imgUltima')[0].complete){
        $("#contenedor1").css("display","block");
    }
    $('#imgUltima').load(function() {
        // Handler for .load() called.
        $("#contenedor1").css("display","block");

    });

    $('.popup-with-zoom-anim').magnificPopup({
        type: 'inline',

        fixedContentPos: false,
        fixedBgPos: true,

        overflowY: 'auto',

        closeBtnInside: true,
        preloader: false,

        midClick: true,
        removalDelay: 300,
        mainClass: 'my-mfp-zoom-in'
    });
});

function mostrar(id){
    $("#"+id).css('display','block');
}

function primerPlano(){
   /* clearInterval(init);
    clearInterval(init1);
    clearInterval(init2);*/
    $(".avanza").css("animationPlayState","paused");
    var distancia = headerWidth -180;

    $( "#arrow_right").hide();

    $( "#lorenzo" ).animate({
        right: "+="+distancia
    }, 9000, function() {
        // Animation complete.
        $.magnificPopup.open({
            items: {
                src: $("#dialog1").html(), // can be a HTML string, jQuery object, or CSS selector
                type: 'inline'
            },
            callbacks: {

                close: function() {
                    // Will fire when popup is closed
                    aparicionLorenzoPrimerPlano();
                }
                // e.t.c.
            },
            modal:true
        });
        //$('.element-with-popup').magnificPopup('open');
        $("#contenedor1").removeClass("avanza");
        $("#contenedor2").removeClass("avanza");
        $("#contenedor3").removeClass("avanza");

        $("#contenedor1").addClass("avanzaReverso");
        $("#contenedor2").addClass("avanzaReverso");
        $("#contenedor3").addClass("avanzaReverso");

    });
}

function aparicionLorenzoPrimerPlano(){

    $("#lorenzo").removeClass("reverso");
    $("#lorenzo").css('left','-200px');
    $("#lorenzo").css('height','380px');
    $("#lorenzo").css('top','180px');
    $("#lorenzo").css('z-index','10');
    $( "#lorenzo" ).animate({
        left: "+=400"
    }, 2500, function() {
        // Animation complete.
        /*init = setInterval("animarBackground(0,'contenedor1',false)", 30);
        init1 = setInterval("animarBackground(1,'contenedor2',false)", 20);
        init2 = setInterval("animarBackground(2,'contenedor3',false)", 15);*/

        $(".avanzaReverso").css("animationPlayState","running");
        var preguntaTime = setTimeout("generar_pregunta()", 5000);

    });
}


function comenzar_juego(){
    var nombre = $("#nombre").val();
    $.ajax({url: "/juego/inscribir_jugador/"+nombre+"/",
        type: 'GET',
        cache: false,
        error: function(xhr) {

            return true;
        },
        success: function(datos){

            if(datos=="error"){
                alert("Debes ingresar un nombre sin caracteres extraños");
            }
            else{
                id_jugador = datos;
                $.magnificPopup.close();
            }
            return true;
        }
    });

}

function generar_pregunta(){
    $("#lorenzo").attr('src','/site_media/images/juego/lorenzo-estatico.png');
    $.ajax({url: "/juego/generar_pregunta/"+id_jugador+"/",
        type: 'GET',
        cache: false,
        error: function(xhr) {

            return true;
        },
        success: function(datos){

            //alert(datos);
            $(".avanzaReverso").css("animationPlayState","paused");
            $.magnificPopup.open({
                items: {
                    src: datos, // can be a HTML string, jQuery object, or CSS selector
                    type: 'inline'
                },
                callbacks: {

                    close: function() {
                        // Will fire when popup is closed
                        $("#lorenzo").attr('src','/site_media/images/juego/lorenzo.gif');
                        $(".avanzaReverso").css("animationPlayState","running");
                        var preguntaTime = setTimeout("generar_pregunta()", 3500);
                    }
                    // e.t.c.
                },
                modal:true
            });
            return true;
        }
    });
}

function siguiente_pregunta(id_pregunta, id_jugador){

    respuesta = $("input:radio[name=group"+id_pregunta+"]:checked").val();
    if(!respuesta){
        alert("Debe seleccionar una respuesta.");
    }
    else{
        $("#estado"+respuesta).show();

        $.ajax({url: "/juego/evaluar_respuesta/"+id_pregunta+"/"+id_jugador+"/"+respuesta+"/",
            type: 'GET',
            cache: false,
            error: function(xhr) {

                return true;
            },
            success: function(datos){
                $( "#btnSiguiente"+id_pregunta ).prop( "disabled", true );
                var cerrarPregunta = setTimeout("$.magnificPopup.close();", 1500);
                $("#lbCorrectas label").html(datos["list"][0]);
                $("#lbFalsas label").html(datos["list"][1]);

            }
        });



    }

}

