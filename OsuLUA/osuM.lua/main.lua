push= require "push"
WINDOW_WIDTH=(love.graphics.getWidth()*2)
WINDOW_HEIGHT=love.graphics.getHeight()+275
spotx={WINDOW_WIDTH/2+40,WINDOW_WIDTH/2+75+40,WINDOW_WIDTH/2-35,WINDOW_WIDTH/2-75-35}
spot=false
speed=1
function love.load()
    math.randomseed=(os.time())
    -- uses nearest naighbot filtering on upscaling and downscaling 
    love.graphics.setDefaultFilter("nearest","nearest")

    smallFont=love.graphics.newFont("font.ttf",8)
    largeFont=love.graphics.newFont("font.ttf",32)
    love.graphics.setFont(smallFont)

    push:setupScreen(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        
        fullscreen=true,
        resizable=false,
        vsync=true
    })
    ballx=100
    bally=0
end

function love.keypressed(key)
    if key == "escape" then
        love.event.quit()
    end
end


function love.update(dt)
    -- player one movement
    if love.keyboard.isDown("n") then
        speed= speed+2
    end
    if love.keyboard.isDown("m") then
        speed= speed-2
    end     
    if love.keyboard.isDown("d") then
        if ballx> WINDOW_WIDTH/2-75-75 and ballx<WINDOW_WIDTH/2-75 then
            spot=false
        end
    end
    if love.keyboard.isDown("f") then
        if ballx> WINDOW_WIDTH/2-75 and ballx<WINDOW_WIDTH/2 then
            spot=false
        end
    end
    if love.keyboard.isDown("j") then
        if ballx> WINDOW_WIDTH/2 and ballx<WINDOW_WIDTH/2+75 then
            spot=false
        end
    end
    if love.keyboard.isDown("k") then
        if ballx> WINDOW_WIDTH/2+75 and ballx<WINDOW_WIDTH/2+75+75 then
            spot=false
        end
    end
    if spot == false then
        ballx=spotx[math.random(4)]
        spot=true
        bally=0
    else
        bally=bally+speed*dt
    end
    if bally >WINDOW_HEIGHT then
        spot= false
    end
end
function love.draw()
    push:apply("start")
    --clear screen and reset
    love.graphics.clear(40,42,52,255)--takes an r,g,b,a val 40 45 52 255 
    love.graphics.line(WINDOW_WIDTH/2,WINDOW_HEIGHT,WINDOW_WIDTH/2,0) 
    love.graphics.line(WINDOW_WIDTH/2+75,WINDOW_HEIGHT,WINDOW_WIDTH/2+75,0) 
    love.graphics.line(WINDOW_WIDTH/2+75+75,WINDOW_HEIGHT,WINDOW_WIDTH/2+75+75,0)
    love.graphics.line(WINDOW_WIDTH/2-75,WINDOW_HEIGHT,WINDOW_WIDTH/2-75,0)
    love.graphics.line(WINDOW_WIDTH/2-75-75,WINDOW_HEIGHT,WINDOW_WIDTH/2-75-75,0)  
    love.graphics.circle('fill',ballx,bally,25)
    push:apply("end")
end