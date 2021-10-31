from cpkf.scan import matrix_scan
import board

col_pins = [board.D8,board.D7,board.D6,board.D5,board.D4, board.MOSI,board.MISO,board.SCK,board.AIN0,board.AIN1]
row_pins = [board.AIN3,board.AIN2, board.D2, board.D3]

Scan = matrix_scan.Scan(row_pins, col_pins, row2col=False)

def layout(kc1,  kc2,  kc3,  kc4,  kc5,     kc6, kc7, kc8, kc9, kc10,
           kc11, kc12, kc13, kc14, kc15,    kc16, kc17, kc18, kc19, kc20,
           kc21, kc22, kc23, kc24, kc25,    kc26, kc27, kc28, kc29, kc30,
           kc31, kc32, kc33, kc34, kc35,    kc36, kc37, kc38, kc39, kc40):
    return [ kc1,  kc2,  kc3,  kc4,  kc5,     kc6, kc7, kc8, kc9, kc10,
           kc11, kc12, kc13, kc14, kc15,    kc16, kc17, kc18, kc19, kc20,
           kc21, kc22, kc23, kc24, kc25,    kc26, kc27, kc28, kc29, kc30,
           kc31, kc32, kc33, kc34, kc35,    kc36, kc37, kc38, kc39, kc40 ]

def layouts(keymaps):
	physical_keymaps = []
	for keymap in keymaps :
		physical_keymaps.append(layout(*keymap))
	
	return physical_keymaps
	
def fs_writable():
    # if you pressed (col0, row0) when booting, you can write firmware.
    row = digitalio.DigitalInOut(board.P1_00)
    row.direction = digitalio.Direction.OUTPUT
    row.value = False
    time.sleep(0.01)
    col = digitalio.DigitalInOut(board.P1_13)
    col.direction = digitalio.Direction.INPUT
    col.pull = digitalio.Pull.UP
    
    return not col.value
