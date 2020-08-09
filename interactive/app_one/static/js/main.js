// Show Form for submitt post
$('#image_post_btn').click(function(){
    $('#video_post').hide();
    $('#image_post').show();
})

$('#video_post_btn').click(function(){
    $('#image_post').hide();
    $('#video_post').show();
    
})
$('#cancel_post_btn').click(function(){
    $('#image_post').hide();
    $('#video_post').hide();
})
