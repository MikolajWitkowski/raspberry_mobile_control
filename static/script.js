$(document).ready(function(){
    var run = false;
            
    var pointer = document.querySelector('.pointer');
    var area = document.querySelector('.area');
    
    var maxX = area.clientWidth - pointer.clientWidth;
    var maxY = area.clientHeight - pointer.clientHeight;
   
    function motionDetection(event){
        var x = event.beta;
        var y = event.gamma;
        
        if(x > 90){
            x = 90;
            };
        if(x < -90){
            x = -90;
            };
            
        x += 90;
        y += 90;
        
        pointer.style.top = (maxX * x / 180 + 25) + 'px';
        pointer.style.left = (maxY * y / 180 + 25) + 'px';
        if (x > 100 &&  (y<100 || y > 80)){
            $('.pointer').addClass('pointer_down')
            $('.pointer').removeClass('pointer_up pointer_left pointer_right')
            }
        if (x < 80 &&  (y<100 || y > 80)){
             $('.pointer').addClass('pointer_up')
             $('.pointer').removeClass('pointer_down pointer_left pointer_right')
            }
        if (y < 80 && (x<100 || x > 80)){
             $('.pointer').addClass('pointer_left')
             $('.pointer').removeClass('pointer_down pointer_up pointer_right')
            }
        if (y > 100 && (x<100 || x > 80)){
             $('.pointer').addClass('pointer_right')
             $('.pointer').removeClass('pointer_down pointer_up pointer_left')
            }
            
        var robotMoveVal = {"x": x, "y": y};
        sendData();
        
        function sendData(){
            $.ajax({
                url: 'robotMove',
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify(robotMoveVal),
                type: 'POST'
                });
            event.preventDefault();
            }   
        }   
    
    $('.start_btn').click(function(){
            if(run == false){
                $('.start_btn').css('background-color', 'red');
                $('.btn_info').html('stop');
                window.addEventListener('deviceorientation', motionDetection);
                run = true;
                }
            else{
                $('.start_btn').css('background-color', 'skyblue');
                $('.btn_info').html('start');
                window.removeEventListener('deviceorientation', motionDetection);
                run = false;
                }
        }); 
});
