from yt_concate.pipeline.steps.get_video_list import Getvideolist
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Getvideolist(),
    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
