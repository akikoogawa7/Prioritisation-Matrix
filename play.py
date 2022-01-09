import distutils
from os import wait
import sys
import asyncio
from utils import quadrant_classifier_label
from matplotlib import pyplot

# create an if statement where we input values based on the number of users voting

async def play():
    # print('\nFind out how to prioritise your objectives...')
    # await asyncio.sleep(4)
    # print('\nAre you ready?')
    # await asyncio.sleep(4)
    # num_of_users = int(input('\nHow many people will be voting?: '))
    # await asyncio.sleep(2)
    # name = input('\nEnter your matrix name: ')
    # await asyncio.sleep(2)
    # print('\nThank you.')
    # await asyncio.sleep(2)
    # problem = input('\nNow enter your problem/objective/question you intend to solve: ')
    # await asyncio.sleep(2)
    # print('\nPerfect.')
    # await asyncio.sleep(1)
    # print('\nNow we need to define the labels for the X and Y AXIS. This should be the metric you wish to measure this against.')
    # await asyncio.sleep(4)
    # print('\nI will give you an example.')
    # await asyncio.sleep(4)
    # print('\nI want to know what my colleagues think about a feature and how feasible it might be.')
    # await asyncio.sleep(4)
    # print('\nBetween 0 to 100, I want to know whether this feature is worth taking onboard.')
    # await asyncio.sleep(4)
    # print("\nI will make the X axis a metric of 'Time', and the Y axis a metric of 'Effort'.")
    # await asyncio.sleep(5)
    # print('\nNow, please enter your X axis label. This should be a label, not a number.')
    # await asyncio.sleep(2)
    x_label = input('\nX axis label: ')
    await asyncio.sleep(2)
    print('\nNow, please enter your Y axis label. This should also be a label, not a number.')
    await asyncio.sleep(2)
    y_label = input('\nY axis label: ')
    await asyncio.sleep(2)
    print('\nNow we need to measure if this is a positive or a negative metric.')
    await asyncio.sleep(4)
    print('\nMeaning, would the increase of this value be good/positive or bad/negative?')
    await asyncio.sleep(4)
    x_polarity = None
    y_polarity = None
    while x_polarity not in ['positive', 'negative']:
        x_polarity = input(f'\nX axis - {x_label} (positive or negative): ')
        if x_polarity in 'positive':
            x_polarity = True
    x_polarity
    await asyncio.sleep(2)
    while y_polarity not in ['positive', 'negative']:
        y_polarity = input(f'\nY axis - {y_label} (positive or negative): ')
        if y_polarity in 'positive':
            y_polarity = True
    y_polarity
    await asyncio.sleep(2)
    print('\nNow we have all the data we need, we will display your matrix.')
    await asyncio.sleep(2)
    preferred_quadrant = quadrant_classifier_label(x_polarity, y_polarity)
    print(f'\nYour preferred quadrant is {preferred_quadrant}.')
    
    # calculate preferred quadrant and allow user to input class name.

    # await input_args()
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(input_args())
    # finally:
    #     loop.close()

if __name__ == '__main__':
    asyncio.run(play())
