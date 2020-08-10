// Show Form for submitt post
$('#image_post_btn').click(function(){
    $('#video_post').hide();
    $('#text_post').hide();
    $('#image_post').show();
})

$('#video_post_btn').click(function(){
    $('#image_post').hide();
    $('#text_post').hide();
    $('#video_post').show();
})

$('#text_post_btn').click(function(){
    $('#image_post').hide();
    $('#video_post').hide();
    $('#text_post').show();
})

$('#cancel_post_btn').click(function(){
    $('#image_post').hide();
    $('#text_post').hide();
    $('#video_post').hide();
})


$('.show_comments').click(function(){
    let pContent=$(this).html()

    if(pContent == 'Hide comments'){
        $(this).html('Show comments')
        $('.display_comment').hide()
    }
    else{
        $(this).html('Hide comments')
        $('.display_comment').show()
    }
})