from flask import Flask

from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return """
    Options:
    type "/shrek"
    type "/bee
    go to https://www.youtube.com/watch?v=dQw4w9WgXcQ
    

    """
@app.route('/shrek')
def shrek():
    return """Once upon a time there was a lovely princess.

But she had an enchantment upon her of a fearful sort which could only 

be broken by love's first kiss.

She was locked away in a castle guarded by a terrible fire-breathing 

dragon.

Many brave knigts had attempted to free her from this dreadful prison, 

but non prevailed.

She waited in the dragon's keep in the highest room of the tallest 

tower for her true love and true love's first kiss.

{Laughing} 

Like that's ever gonna happen.

{Paper Rusting, Toilet Flushes}

What a load of - 



Somebody once told me the world is gonna roll me

I ain't the sharpest tool in the shed

She was lookin' kind of dumb with her finger and her thumb

In the shape of an "L" on her forehead

The years start comin' and they don't stop comin'

Fed to the rules and hit the ground runnin'

Didn't make sense not to live for fun

Your brain gets smart but your head gets dumb

So much to do so much to see

So what's wrong with takin' the backstreets

You'll never know if you don't go

You'll never shine if you don't glow

Hey, now You're an all-star

Get your game on, go play

Hey, now You're a rock star

Get the show on, get paid

And all that glitters is gold

Only shootin' stars break the mold

It's a cool place and they say it gets colder

You're bundled up now but wait till you get older

But the meteor men beg to differ

Judging by the hole in the satellite picture

The ice we skate is gettin' pretty thin

The water's getting warm so you might as well swim

My world's on fire

How 'bout yours

That's the way I like it and I'll never get bored

Hey, now, you're an all-star

{Shouting}

Get your game on, go play

Hey, now You're a rock star

Get the show on, get paid

And all that glitters is gold

Only shootin' stars break the mold
    
    """
    
@app.route('/bee')
def bee():
    return """According to all known laws
of aviation,

  
there is no way a bee
should be able to fly.

  
Its wings are too small to get
its fat little body off the ground.

  
The bee, of course, flies anyway

  
because bees don't care
what humans think is impossible. 



"""