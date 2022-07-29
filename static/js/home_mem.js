
let textEl = $('.answer').text()
console.log(textEl)
function voteChange(){
  textEl = $('.answer').text()
  if (textEl == "sunny is selected..."){
    $('.govote').css("display","none")
    console.log("sunny")
    $('.user').attr("style","background-image: url('/static/image/sunny.gif')")
    $('.user .home_icon').attr("src","/static/image/sunny_icon.gif")
  }
  else if (textEl == "rainny is selected..."){
    $('.govote').css("display","none")
    console.log("rainny")
    $('.user').attr("style","background-image: url('/static/image/rainy.gif')")
    $('.user .home_icon').attr("src","/static/image/rainy_icon.gif")
  }
  else if (textEl == "snow is selected..."){
    $('.govote').css("display","none")
    console.log("snow")
    $('.user').attr("style","background-image: url('/static/image/snow.gif')")
    $('.user .home_icon').attr("src","/static/image/snow_icon.gif")
  }
}

setInterval(() => voteChange(), 1000);