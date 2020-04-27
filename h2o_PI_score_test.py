###### ON THE RASPBERRY ###########################################################################

# region ########## imports and setup #############################################################
import h2o
import pandas as pd

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial,cascaded=4, block_orientation=-90)

# endregion #######################################################################################


#region ########### example score #################################################################

car_to_score = pd.DataFrame({"ouderdom":[3], "KM":[40000]})

## importtant to set java_options = "-Xmx100m", the default value is too large the PI 
price = h2o.mojo_predict_pandas(
    car_to_score,
    mojo_zip_path = "StackedEnsemble_AllModels_AutoML_20200426_221740.zip",
    java_options = "-Xmx100m"
)

pr = round(price.predict.values[0])

# display on led matrix
full_msg = f"predicted car price = {pr}"
show_message(device, full_msg , fill="white", font=proportional(CP437_FONT), scroll_delay=0.07)

#endregion ########################################################################################