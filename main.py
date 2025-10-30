from kokoro.pipeline import KPipeline
import logging
import time

logger = logging.getLogger(__name__)

# load the model and warm up run
pipeline = KPipeline(lang_code='h',device="cuda")
for i in pipeline("जीवन एक यात्रा है, जहाँ हर अनुभव हमें सिखाता है कि हारना अंत नहीं, नई शुरुआत है। जीवन एक यात्रा है, जहाँ हर अनुभव हमें सिखाता है कि हारना अंत नहीं, नई शुरुआत है।",voice="hf_alpha"):
    pass

start,end,sum=0,0,0

for i in range(500):
    start = time.time_ns()
    for output in pipeline("जीवन एक यात्रा है, जहाँ हर अनुभव हमें सिखाता है कि हारना अंत नहीं, नई शुरुआत है। जीवन एक यात्रा है, जहाँ हर अनुभव हमें सिखाता है कि हारना अंत नहीं, नई शुरुआत है।",voice="hf_alpha"):
        pass
    end = time.time_ns()
    sum += (end - start)
    logger.warning(f"Time taken for iteration {i}: {(end - start)*10e6} milliseconds")

logger.warning(f"Average Time taken: {(sum/500)*10e6} milliseconds")
