push= require "push"
WINDOW_WIDTH=(love.graphics.getWidth()*2)
WINDOW_HEIGHT=love.graphics.getHeight()+275
function incircle(cx, cy, radius, x, y)
    dx = cx - x
    dy = cy - y
    return dx * dx + dy * dy <= radius * radius
end


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
    ball=true
    p1score=0
    ring=75
    ballx=math.random(0,WINDOW_WIDTH/2)
    bally=math.random(0,WINDOW_HEIGHT/2)
end

function love.keypressed(key)
    if key == "escape" then
        love.event.quit()
    end
end



function love.update(dt)
    -- player one movement
    if love.keyboard.isDown("space") then
        ballx=math.random(0,WINDOW_WIDTH-30)
        bally=math.random(0,WINDOW_HEIGHT-30)
        ring=75
    end
    if ring == 0 then
        ballx=math.random(0,WINDOW_WIDTH-30)
        bally=math.random(0,WINDOW_HEIGHT-30)
        ring=75
    end
end

function love.mousepressed(x,y,button) 
    if incircle(ballx,bally,ring,x,y) and button == 1 then
        ballx=math.random(0,WINDOW_WIDTH-30)
        bally=math.random(0,WINDOW_HEIGHT-30)
        ring=75 
    end
end

--love.graphics.circle( mode, x, y, radius )
function love.draw()
    push:apply("start")
    --clear screen and reset
    love.graphics.clear(40,42,52,255)--takes an r,g,b,a val 40 45 52 255 
    love.graphics.circle('fill',ballx,bally,25)-- filled or not/need to know start x,y/ end x,y
    if ring ~= 0 then
        ring=ring-1
    end
    love.graphics.circle('line',ballx,bally,ring)
    push:apply("end")
end