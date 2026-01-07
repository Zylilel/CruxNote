def techniques():
    while True:
        techniquesoption = input(
            "What are you interested in?\n"
            "(1) Center of Gravity Manipulation\n"
            "(2) Foot Techniques\n"
            "(3) Hand Techniques\n"
            "(4) Climbing Positions\n"
            "(5) Movement Techniques\n"
            "(6) Dyno Techniques\n"
            "(Q) Quit\n- "
        ).strip()
        if techniquesoption == "1":
            center_of_gravity_manipulation()
        elif techniquesoption == "2":
            foot_techniques()
        elif techniquesoption == "3":
            hand_techniques()
        elif techniquesoption == "4":
            climbing_positions()
        elif techniquesoption == "5":
            movement_techniques()
        elif techniquesoption == "6":
            dynamic_techniques()
        elif techniquesoption.lower() == "q":
            break
        else:
            print("Please enter a valid option.")


def center_of_gravity_manipulation():
    print("""Center of Gravity Manipulating
Back step: The back step is when you turn in to get your center of gravity closer to the wall. In this case, you're standing on the outside of one of your feet.

Drop knee: The drop knee is a more extreme version of the back step, and it involves turning in so far that your knee points down.

Outside flag: The outside flag is when your outside leg sticks in front of you and keeps you in balance that way.

Back flag: The back flag is when the other leg sticks behind you to keep you in balance.

Inside flag: The inside flag is when the other leg sticks in front of you to keep you in balance.

Inside figure 4: The inside figure four is a way to get a little bit higher by wrapping your leg on top of your arm. Pro tip, when you're doing a figure four, get your one leg over your hand. Push with your other on the wall to get your hips as high as possible.

Outside figure 4: The outside figure four is very similar to the inside, except you wrap your other leg on top of your arm. And that's a great way to reach sideways.

Arm flag: The arm flag is anytime you shift your center of gravity around by moving your arm.

Perching: Perching is anytime you sit on top of your heel while the other leg is extended. It's a great way to rest.

Frogging: Frogging is both of your legs are bent and you sit on both of your heels at the same time

Scorpion: The scorpion is a way to stay relatively close to the wall in a dynamic move. You let your leg swing back, and that will actually keep your body relatively close to the wall.

Janja: The Janja is very similar to the scorpion except for movements that are sideways. (It works much better if you have long blonde hair.)

Peter Pan: The Peter Pan is another way to control the swing in a dynamic move by swing. Same like the scorpion but you move 1 legs at a time instead of both.
""")
    input("\nPress Enter to return to the main menu...")

def foot_techniques():
    print("""Foot Techniques
Toe-ing: The Toe-ing is one of the most basic yet important foot technique in climbing in general. This involves pointing the toes downward, and presisng the edge of the toes into the surface of the rock or wall.

Inside edge: The inside edge is when you stand on the inside of your climbing shoe. As you stand, most of the pressure will be on your big toe.

Outside edge: The outside edge is quite similar to the inside edge, except you will stand on the outside of your climbing shoe. But yet again, most of the force will be on your big toe.

Smearing: Smearing is when you lower your heel so that you increase the amount of surface area on the foot hold. Pro tip! Stand as far away from the wall as possible. So you have more room to lean in. So the angle actually gets more positive when you're standing on the edge of the volume instead of close to the wall.

Alpine knee: The Alpine knee is anytime you use your knee and push on a foot hold. For some reason, this technique is frowned upon in the climbing community.

Heel hook: The heel hook is anytime you use your heel on a foothold, often to pull in or to push up. Pro tip! you get your heel behind the hold, and then you actually turn it to the wall and down. So you can really get your knee really high, get your knee a bit over your foot, and get your hips as high as possible so that you can make use of your leg power instead of your arm power.

Toe hook: The toe hook is when you stick the top of your foot behind a climbing hold in order to stick the position. This is often with a straight leg.

Bat hang: The bat hang is when you hang upside down using the rubber on the top of your shoe, often with two feet

Bicycle: The bicycle is when you push with one foot and pull with the other, so you combine a toe hook with a pushing movement.

Heel-toe cam: The heel-toe cam is an overlooked technique where you jam your foot between two holds.

Frog pinch: The frog pinch is when you squeeze with both of your feet on a vertical hold.

Knee bar: The knee bar is a great position where you try to jam your thigh behind a hold. If done well, then you can actually let go of both of your arms. But unfortunately, that's not always the case.
""")
    input("\nPress Enter to return to the main menu...")

def hand_techniques():
    print("""Hand Techniques
3 finger drag: In a three-finger drag, you use three fingers in the most open position possible.

Open crimp: In the open crimp, you add the pinky, but still the hand is as open as possible.

Quarter crimp: A quarter crimp is a really weird technique where your hand is in an open position, but you add your thumb anyway to get a little bit more leverage.

Half crimp: In the half crimp, the knuckle is at the same height as the fingertip. The half crimp can be done with the front three fingers or with the back three fingers as well. Just make sure that the knuckle is at the same height as the fingertip.

Full crimp: In the closed crimp, the thumb is added on top of the fingertip for more power.

2 finger pocket: The two-finger pocket could either be with the middle two fingers, with the front two fingers, or with the back two fingers. It doesn't matter as long as you add two fingers and keep your hands open.

Stacked fingers: The stacked fingers is anytime you stack your fingers in order to fit more fingers into the pocket.

Mono pocket: The mono pocket is when you can only fit one finger into the pocket. When you close down on the mono with your thumb, it's called the closed mono, and this technique is very injury prone. Be careful.

Pinch: The pinch is when you grab a hold by squeezing it between your thumb and your fingers.

Thumbercling: The thumbercling is when you use your thumb to press down on the hold. This is a great technique to use on a slab.

Palm down: The palm down is when you press down on a climbing hold. Usually, your fingers will point out.

Meat hook: The meat hook is when you wrap your hand all the way around the climbing hold. You can also wrap your hands around the volume.
""")
    input("\nPress Enter to return to the main menu...")

def climbing_positions():
    print("""Climbing Positions
Side pull: In the side pull position, you will pull inwards with your arm and press in the opposite direction with your feet.

Layback: A more extreme version of the sidepull, often performed in a crack on an arête or on a big feature like on this one.

Gaston: The gaston is essentially the opposite of the side pull. You will press outwards with your arm and keep the position in that way.

Elevator: A double gaston is often called an elevator door. You will press outwards with both of your arms at the same time

Undercling: The undercling is when you push up with the feet and press down with one or both of your arms.

Compression: Compression is anytime you use your hands and feet to pull inwards and create compression in order to keep the position in that way.

Inverted: Inverted is anytime your feet are above the body. This is the position you need in order to climb feet first.

Outwards facing: Outwards facing is anytime you face away from the wall. 

Gastondercling: If you have an undercling position with your elbow pointed out, then this position is called the gastondercling.

Lock off: The lock off is when you bend your arm to pull in the wall and up in order to reach for the next hold.

Stemming: Stemming is anytime you press outwards with your feet in order to keep the position. This is a great time to shake your hands and rest.

Chin: A very mystical technique on a slab in which you put your chin on the hold to rest your hand. No demonstration for obvious reasons. The closest I could find as a demonstration is from the Climbing Stuff channel (https://www.youtube.com/shorts/MQnGin9aung?feature=share)
""")
    input("\nPress Enter to return to the main menu...")

def movement_techniques():
    print("""Movement Techniques
Foot match & switch: Matching feet is when you put one foot on the same hold as the other, often to switch feet. You can do the same with your hands, putting your hands on the same hold in order to switch.

Hands match & switch: You can do the same with your hands, putting your hands on the same hold in order to switch.

Piano match & switch:When you switch one finger at a time on the climbing hold, this is called the piano match and switch.

Houdini: The Houdini is a very fancy technique where you let go of the hold and quickly grab it with the other hand before you have time to fall.

Hand foot match: The hand-foot match is whenever you put your foot on the same hold as your hand in order to switch. This can be done on a slab or in an overhang. It doesn't matter.

Hand flip: The hand flip is when you pull in one direction and then you quickly flip directions so you can pull in the other.

Hand crossover: The hand cross can be done either over or under the other arm.

Rose move: A very extreme version of the hand cross under is called the rose move, and this is a very fancy technique that is often done on World Cups.

Foot cross: The foot cross can be done either in front or behind the other foot.

Good samaritan: The Good Samaritan is often done by people who aren't flexible. They can pull on their leg in order to reach the next hold.

Knee press: The knee press is when you press down on your knee in order to stand up a little bit more easily.

Rock over: The rock over is when you pull on your foot and get your center of gravity all the way over onto your leading foot.

Cut loose: The cut loose is when you let go of your feet on the climbing wall and you hang only on your arms.

Campussing: When you climb using only your arms, this is called campussing.

T-rex, turtle, roll (What is this name): T-rex, turtle, roll is the most important technique for indoor boulderers. This will help you prevent injuries by landing on your feet, then immediately lying back to reduce the impact.

Mantle: Mantling is anytime you get on top of a ledge or the top of the boulder by pushing your body upwards with your triceps.
""")
    input("\nPress Enter to return to the main menu...")

def dynamic_techniques():
    print("""Dynamic techniques
Dyno: A dyno is when you jump, lose contact with the wall, and then grab the next hold with both your hands.

1 arm dyno: Same as a dyno but you grab the next hold with one arm.

Double clutch: The double clutch is when you grab two different holds or the same hold with two different hand techniques at the same time.

Double dyno: The double dyno is when you move from one hold onto the next.

Paddle dyno: The paddle dyno is a more extreme version of dyno where you keep moving up and up. This can be a triple or a quadruple dyno.

Step up dyno: In a step-up dyno, you try to jump a little bit higher by getting your foot up and then jumping again.

Hip swing: Another way to jump a little bit higher is by creating momentum. One of the ways to do this is by swinging with your hips.

 Arm swing: Same as hip swing, but using arm.

Pogo: The pogo is when you create momentum using your leg. This is also called a moon kick.

Run & jump: The run and jump is when you reach the next hold by running and then, obviously, jumping.

Swing & jump: The swing and jump is when you swing from a hold and then jump in the air in order to latch on to the next hold.

Deadpoint: The deadpoint is a dynamic move where you go just high enough in order to grab the next hold. When done correctly, you will grab the next hold while you're not moving up or down at all. Instead, you will stick the move just when you're suspended in mid-air.

Headbutt: Use your head to create momentum lol.
""")
    input("\nPress Enter to return to the main menu...")
