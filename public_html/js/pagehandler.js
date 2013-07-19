
$(document).ready( function(){

  $('.garden-page').click( function(event){
    event.preventDefault();
    var move_window     = $( '.move_box' );
    var url             = $(this).attr( 'href' );
    var doc_height      = $(document).height();

    $.each( $('.nav li a'), function(){
      if( $(this).attr('href') == url ){
        $(this).parent().addClass('active')
      } else {
        $(this).parent().removeClass('active')
      }
    } );
  
    $.ajax({
      url: url
    }).done( function( html ) {
      html    = $( html );
      html.addClass( 'stage_next' );
      html.css( 'top', doc_height + 'px' );
      $( "#move_container" ).append(html);
      new_content = $( '.stage_next' );
      animate_window_in( new_content );
      animate_window_out( move_window  );

    })
  
  });

});

function animate_window_out( remove_div ){
  remove_div.css( 'position', 'relative' );
  remove_div.animate( {
      top: '-'+ remove_div.height() +'px'
  }, 500, function() {
      remove_div.remove();
  });
}

function animate_window_in( add_div ){
  add_div.hide();
  add_div.fadeIn( 750 ); //@todo: do this with opacity                                                                                                                                                                           
  add_div.animate({
      top: '0px'
  }, 750 );
  add_div.removeClass('stage_next');
  add_div.addClass('move_box');
}