'''
    XBMC LCDproc addon
    Copyright (C) 2012 Team XBMC
    
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

encmap_hd44780_a00 = {
  0x0000: 0x0000,     #  NULL
  # 0x0001: 0x0001,     #  START OF HEADING
  # 0x0002: 0x0002,     #  START OF TEXT
  # 0x0003: 0x0003,     #  END OF TEXT
  # 0x0004: 0x0004,     #  END OF TRANSMISSION
  # 0x0005: 0x0005,     #  ENQUIRY
  # 0x0006: 0x0006,     #  ACKNOWLEDGE
  # 0x0007: 0x0007,     #  BELL
  # 0x0008: 0x0008,     #  BACKSPACE
  # 0x0009: 0x0009,     #  HORIZONTAL TABULATION
  # 0x000a: 0x000a,     #  LINE FEED
  # 0x000b: 0x000b,     #  VERTICAL TABULATION
  # 0x000c: 0x000c,     #  FORM FEED
  # 0x000d: 0x000d,     #  CARRIAGE RETURN
  # 0x000e: 0x000e,     #  SHIFT OUT
  # 0x000f: 0x000f,     #  SHIFT IN
  # 0x0010: 0x0010,     #  DATA LINK ESCAPE
  # 0x0011: 0x0011,     #  DEVICE CONTROL ONE
  # 0x0012: 0x0012,     #  DEVICE CONTROL TWO
  # 0x0013: 0x0013,     #  DEVICE CONTROL THREE
  # 0x0014: 0x0014,     #  DEVICE CONTROL FOUR
  # 0x0015: 0x0015,     #  NEGATIVE ACKNOWLEDGE
  # 0x0016: 0x0016,     #  SYNCHRONOUS IDLE
  # 0x0017: 0x0017,     #  END OF TRANSMISSION BLOCK
  # 0x0018: 0x0018,     #  CANCEL
  # 0x0019: 0x0019,     #  END OF MEDIUM
  # 0x001a: 0x001a,     #  SUBSTITUTE
  # 0x001b: 0x001b,     #  ESCAPE
  # 0x001c: 0x001c,     #  INFORMATION SEPARATOR FOUR
  # 0x001d: 0x001d,     #  INFORMATION SEPARATOR THREE
  # 0x001e: 0x001e,     #  INFORMATION SEPARATOR TWO
  # 0x001f: 0x001f,     #  INFORMATION SEPARATOR ONE
  0x0020: 0x0020,     #  SPACE
  0x0021: 0x0021,     #  EXCLAMATION MARK
  0x0022: 0x0022,     #  QUOTATION MARK
  0x0023: 0x0023,     #  NUMBER SIGN
  0x0024: 0x0024,     #  DOLLAR SIGN
  0x0025: 0x0025,     #  PERCENT SIGN
  0x0026: 0x0026,     #  AMPERSAND
  0x0027: 0x0027,     #  APOSTROPHE
  0x0028: 0x0028,     #  LEFT PARENTHESIS
  0x0029: 0x0029,     #  RIGHT PARENTHESIS
  0x002a: 0x002a,     #  ASTERISK
  0x002b: 0x002b,     #  PLUS SIGN
  0x002c: 0x002c,     #  COMMA
  0x002d: 0x002d,     #  HYPHEN-MINUS
  0x002e: 0x002e,     #  FULL STOP
  0x002f: 0x002f,     #  SOLIDUS
  0x0030: 0x0030,     #  DIGIT ZERO
  0x0031: 0x0031,     #  DIGIT ONE
  0x0032: 0x0032,     #  DIGIT TWO
  0x0033: 0x0033,     #  DIGIT THREE
  0x0034: 0x0034,     #  DIGIT FOUR
  0x0035: 0x0035,     #  DIGIT FIVE
  0x0036: 0x0036,     #  DIGIT SIX
  0x0037: 0x0037,     #  DIGIT SEVEN
  0x0038: 0x0038,     #  DIGIT EIGHT
  0x0039: 0x0039,     #  DIGIT NINE
  0x003a: 0x003a,     #  COLON
  0x003b: 0x003b,     #  SEMICOLON
  0x003c: 0x003c,     #  LESS-THAN SIGN
  0x003d: 0x003d,     #  EQUALS SIGN
  0x003e: 0x003e,     #  GREATER-THAN SIGN
  0x003f: 0x003f,     #  QUESTION MARK
  0x0040: 0x0040,     #  COMMERCIAL AT
  0x0041: 0x0041,     #  LATIN CAPITAL LETTER A
  0x0042: 0x0042,     #  LATIN CAPITAL LETTER B
  0x0043: 0x0043,     #  LATIN CAPITAL LETTER C
  0x0044: 0x0044,     #  LATIN CAPITAL LETTER D
  0x0045: 0x0045,     #  LATIN CAPITAL LETTER E
  0x0046: 0x0046,     #  LATIN CAPITAL LETTER F
  0x0047: 0x0047,     #  LATIN CAPITAL LETTER G
  0x0048: 0x0048,     #  LATIN CAPITAL LETTER H
  0x0049: 0x0049,     #  LATIN CAPITAL LETTER I
  0x004a: 0x004a,     #  LATIN CAPITAL LETTER J
  0x004b: 0x004b,     #  LATIN CAPITAL LETTER K
  0x004c: 0x004c,     #  LATIN CAPITAL LETTER L
  0x004d: 0x004d,     #  LATIN CAPITAL LETTER M
  0x004e: 0x004e,     #  LATIN CAPITAL LETTER N
  0x004f: 0x004f,     #  LATIN CAPITAL LETTER O
  0x0050: 0x0050,     #  LATIN CAPITAL LETTER P
  0x0051: 0x0051,     #  LATIN CAPITAL LETTER Q
  0x0052: 0x0052,     #  LATIN CAPITAL LETTER R
  0x0053: 0x0053,     #  LATIN CAPITAL LETTER S
  0x0054: 0x0054,     #  LATIN CAPITAL LETTER T
  0x0055: 0x0055,     #  LATIN CAPITAL LETTER U
  0x0056: 0x0056,     #  LATIN CAPITAL LETTER V
  0x0057: 0x0057,     #  LATIN CAPITAL LETTER W
  0x0058: 0x0058,     #  LATIN CAPITAL LETTER X
  0x0059: 0x0059,     #  LATIN CAPITAL LETTER Y
  0x005a: 0x005a,     #  LATIN CAPITAL LETTER Z
  0x005b: 0x005b,     #  LEFT SQUARE BRACKET
  0x005c: 0x00a4,     #  REVERSE SOLIDUS
  0x005d: 0x005d,     #  RIGHT SQUARE BRACKET
  0x005e: 0x005e,     #  CIRCUMFLEX ACCENT
  0x005f: 0x005f,     #  LOW LINE
  0x0060: 0x0060,     #  GRAVE ACCENT
  0x0061: 0x0061,     #  LATIN SMALL LETTER A
  0x0062: 0x0062,     #  LATIN SMALL LETTER B
  0x0063: 0x0063,     #  LATIN SMALL LETTER C
  0x0064: 0x0064,     #  LATIN SMALL LETTER D
  0x0065: 0x0065,     #  LATIN SMALL LETTER E
  0x0066: 0x0066,     #  LATIN SMALL LETTER F
  0x0067: 0x0067,     #  LATIN SMALL LETTER G
  0x0068: 0x0068,     #  LATIN SMALL LETTER H
  0x0069: 0x0069,     #  LATIN SMALL LETTER I
  0x006a: 0x006a,     #  LATIN SMALL LETTER J
  0x006b: 0x006b,     #  LATIN SMALL LETTER K
  0x006c: 0x006c,     #  LATIN SMALL LETTER L
  0x006d: 0x006d,     #  LATIN SMALL LETTER M
  0x006e: 0x006e,     #  LATIN SMALL LETTER N
  0x006f: 0x006f,     #  LATIN SMALL LETTER O
  0x0070: 0x0070,     #  LATIN SMALL LETTER P
  0x0071: 0x0071,     #  LATIN SMALL LETTER Q
  0x0072: 0x0072,     #  LATIN SMALL LETTER R
  0x0073: 0x0073,     #  LATIN SMALL LETTER S
  0x0074: 0x0074,     #  LATIN SMALL LETTER T
  0x0075: 0x0075,     #  LATIN SMALL LETTER U
  0x0076: 0x0076,     #  LATIN SMALL LETTER V
  0x0077: 0x0077,     #  LATIN SMALL LETTER W
  0x0078: 0x0078,     #  LATIN SMALL LETTER X
  0x0079: 0x0079,     #  LATIN SMALL LETTER Y
  0x007a: 0x007a,     #  LATIN SMALL LETTER Z
  0x007b: 0x007b,     #  LEFT CURLY BRACKET
  0x007c: 0x007c,     #  VERTICAL LINE
  0x007d: 0x007d,     #  RIGHT CURLY BRACKET
  0x007e: 0x00b0,     #  TILDE
  0x007f: 0x0020,     #  DELETE
  0x0080: 0x0020,
  0x0081: 0x0020,
  0x0082: 0x002c,
  0x0083: 0x0020,
  0x0084: 0x0022,
  0x0085: 0x0020,
  0x0086: 0x0020,
  0x0087: 0x0020,
  0x0088: 0x005e,
  0x0089: 0x0020,
  0x008a: 0x0053,
  0x008b: 0x003c,
  0x008c: 0x0020,
  0x008d: 0x0020,
  0x008e: 0x005a,
  0x008f: 0x0020,
  0x0090: 0x0020,
  0x0091: 0x0027,
  0x0092: 0x0027,
  0x0093: 0x0022,
  0x0094: 0x0022,
  0x0095: 0x00a5,
  0x0096: 0x00b0,
  0x0097: 0x00b0,
  0x0098: 0x00b0,
  0x0099: 0x0020,
  0x009a: 0x0073,
  0x009b: 0x003e,
  0x009c: 0x0020,
  0x009d: 0x0020,
  0x009e: 0x007a,
  0x009f: 0x0059,
  0x00a0: 0x00ff,     #  NO-BREAK SPACE
  0x00a1: 0x0021,     #  INVERTED EXCLAMATION MARK
  0x00a2: 0x0020,     #  CENT SIGN
  0x00a3: 0x0020,     #  POUND SIGN
  0x00a4: 0x0020,     #  CURRENCY SIGN
  0x00a5: 0x005c,     #  YEN SIGN
  0x00a6: 0x007c,     #  BROKEN BAR
  0x00a7: 0x0020,     #  SECTION SIGN
  0x00a8: 0x0022,     #  DIAERESIS
  0x00a9: 0x0020,     #  COPYRIGHT SIGN
  0x00aa: 0x0020,     #  FEMININE ORDINAL INDICATOR
  0x00ab: 0x00ff,     #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
  0x00ac: 0x000e,     #  NOT SIGN -- FIXME?
  0x00ad: 0x000a,     #  SOFT HYPHEN -- FIXME?
  0x00ae: 0x0009,     #  REGISTERED SIGN -- FIXME?
  0x00af: 0x0008,     #  MACRON -- FIXME?
  0x00b0: 0x00df,     #  DEGREE SIGN
  0x00b1: 0x0020,     #  PLUS-MINUS SIGN
  0x00b2: 0x0020,     #  SUPERSCRIPT TWO
  0x00b3: 0x0020,     #  SUPERSCRIPT THREE
  0x00b4: 0x0027,     #  ACUTE ACCENT
  0x00b5: 0x00e4,     #  MICRO SIGN
  0x00b6: 0x0020,     #  PILCROW SIGN
  0x00b7: 0x00a5,     #  MIDDLE DOT
  0x00b8: 0x0020,     #  CEDILLA
  0x00b9: 0x0020,     #  SUPERSCRIPT ONE
  0x00ba: 0x00df,     #  MASCULINE ORDINAL INDICATOR
  0x00bb: 0x003e,     #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
  0x00bc: 0x0020,     #  VULGAR FRACTION ONE QUARTER
  0x00bd: 0x0020,     #  VULGAR FRACTION ONE HALF
  0x00be: 0x0020,     #  VULGAR FRACTION THREE QUARTERS
  0x00bf: 0x003f,     #  INVERTED QUESTION MARK
  0x00c0: 0x0041,     #  LATIN CAPITAL LETTER A WITH GRAVE
  0x00c1: 0x0041,     #  LATIN CAPITAL LETTER A WITH ACUTE
  0x00c2: 0x0041,     #  LATIN CAPITAL LETTER A WITH CIRCUMFLEX
  0x00c3: 0x0041,     #  LATIN CAPITAL LETTER A WITH TILDE
  0x00c4: 0x0041,     #  LATIN CAPITAL LETTER A WITH DIAERESIS
  0x00c5: 0x0041,     #  LATIN CAPITAL LETTER A WITH RING ABOVE
  0x00c6: 0x0020,     #  LATIN CAPITAL LETTER AE
  0x00c7: 0x0043,     #  LATIN CAPITAL LETTER C WITH CEDILLA
  0x00c8: 0x0045,     #  LATIN CAPITAL LETTER E WITH GRAVE
  0x00c9: 0x0045,     #  LATIN CAPITAL LETTER E WITH ACUTE
  0x00ca: 0x0045,     #  LATIN CAPITAL LETTER E WITH CIRCUMFLEX
  0x00cb: 0x0045,     #  LATIN CAPITAL LETTER E WITH DIAERESIS
  0x00cc: 0x0049,     #  LATIN CAPITAL LETTER I WITH GRAVE
  0x00cd: 0x0049,     #  LATIN CAPITAL LETTER I WITH ACUTE
  0x00ce: 0x0049,     #  LATIN CAPITAL LETTER I WITH CIRCUMFLEX
  0x00cf: 0x0049,     #  LATIN CAPITAL LETTER I WITH DIAERESIS
  0x00d0: 0x0044,     #  LATIN CAPITAL LETTER ETH
  0x00d1: 0x004e,     #  LATIN CAPITAL LETTER N WITH TILDE
  0x00d2: 0x004f,     #  LATIN CAPITAL LETTER O WITH GRAVE
  0x00d3: 0x004f,     #  LATIN CAPITAL LETTER O WITH ACUTE
  0x00d4: 0x004f,     #  LATIN CAPITAL LETTER O WITH CIRCUMFLEX
  0x00d5: 0x004f,     #  LATIN CAPITAL LETTER O WITH TILDE
  0x00d6: 0x004f,     #  LATIN CAPITAL LETTER O WITH DIAERESIS
  0x00d7: 0x0078,     #  MULTIPLICATION SIGN
  0x00d8: 0x0030,     #  LATIN CAPITAL LETTER O WITH STROKE
  0x00d9: 0x0055,     #  LATIN CAPITAL LETTER U WITH GRAVE
  0x00da: 0x0055,     #  LATIN CAPITAL LETTER U WITH ACUTE
  0x00db: 0x0055,     #  LATIN CAPITAL LETTER U WITH CIRCUMFLEX
  0x00dc: 0x0055,     #  LATIN CAPITAL LETTER U WITH DIAERESIS
  0x00dd: 0x0059,     #  LATIN CAPITAL LETTER Y WITH ACUTE
  0x00de: 0x0020,     #  LATIN CAPITAL LETTER THORN
  0x00df: 0x00e2,     #  LATIN SMALL LETTER SHARP
  0x00e0: 0x0061,     #  LATIN SMALL LETTER A WITH GRAVE
  0x00e1: 0x0061,     #  LATIN SMALL LETTER A WITH ACUTE
  0x00e2: 0x0061,     #  LATIN SMALL LETTER A WITH CIRCUMFLEX
  0x00e3: 0x0061,     #  LATIN SMALL LETTER A WITH TILDE
  0x00e4: 0x00e1,     #  LATIN SMALL LETTER A WITH DIAERESIS
  0x00e5: 0x0061,     #  LATIN SMALL LETTER A WITH RING ABOVE
  0x00e6: 0x0020,     #  LATIN SMALL LETTER AE
  0x00e7: 0x0063,     #  LATIN SMALL LETTER C WITH CEDILLA
  0x00e8: 0x0065,     #  LATIN SMALL LETTER E WITH GRAVE
  0x00e9: 0x0065,     #  LATIN SMALL LETTER E WITH ACUTE
  0x00ea: 0x0065,     #  LATIN SMALL LETTER E WITH CIRCUMFLEX
  0x00eb: 0x0065,     #  LATIN SMALL LETTER E WITH DIAERESIS
  0x00ec: 0x0069,     #  LATIN SMALL LETTER I WITH GRAVE
  0x00ed: 0x0069,     #  LATIN SMALL LETTER I WITH ACUTE
  0x00ee: 0x0069,     #  LATIN SMALL LETTER I WITH CIRCUMFLEX
  0x00ef: 0x0069,     #  LATIN SMALL LETTER I WITH DIAERESIS
  0x00f0: 0x006f,     #  LATIN SMALL LETTER ETH
  0x00f1: 0x006e,     #  LATIN SMALL LETTER N WITH TILDE
  0x00f2: 0x006f,     #  LATIN SMALL LETTER O WITH GRAVE
  0x00f3: 0x006f,     #  LATIN SMALL LETTER O WITH ACUTE
  0x00f4: 0x006f,     #  LATIN SMALL LETTER O WITH CIRCUMFLEX
  0x00f5: 0x006f,     #  LATIN SMALL LETTER O WITH TILDE
  0x00f6: 0x00ef,     #  LATIN SMALL LETTER O WITH DIAERESIS
  0x00f7: 0x00fd,     #  DIVISION SIGN
  0x00f8: 0x006f,     #  LATIN SMALL LETTER O WITH STROKE
  0x00f9: 0x0075,     #  LATIN SMALL LETTER U WITH GRAVE
  0x00fa: 0x0075,     #  LATIN SMALL LETTER U WITH ACUTE
  0x00fb: 0x0075,     #  LATIN SMALL LETTER U WITH CIRCUMFLEX
  0x00fc: 0x00f5,     #  LATIN SMALL LETTER U WITH DIAERESIS
  0x00fd: 0x0079,     #  LATIN SMALL LETTER Y WITH ACUTE
  0x00fe: 0x0020,     #  LATIN SMALL LETTER THORN
  0x00ff: 0x0079,     #  LATIN SMALL LETTER Y WITH DIAERESIS
# Polish letters mapping replacements
  0x0104: 0x0041,     #  LATIN CAPITAL LETTER A WITH OGONEK
  0x0105: 0x0061,     #  LATIN SMALL LETTER A WITH OGONEK
  0x0106: 0x0043,     #  LATIN CAPITAL LETTER C WITH ACUTE
  0x0107: 0x0063,     #  LATIN SMALL LETTER C WITH ACUTE
  0x0118: 0x0045,     #  LATIN CAPITAL LETTER E WITH OGONEK
  0x0119: 0x0065,     #  LATIN SMALL LETTER E WITH OGONEK
  0x0141: 0x004c,     #  LATIN CAPITAL LETTER L WITH STROKE
  0x0142: 0x006c,     #  LATIN SMALL LETTER L WITH STROKE
  0x0143: 0x004e,     #  LATIN CAPITAL LETTER N WITH ACUTE
  0x0144: 0x006e,     #  LATIN SMALL LETTER N WITH ACUTE
  0x015a: 0x0053,     #  LATIN CAPITAL LETTER S WITH ACUTE
  0x015b: 0x0073,     #  LATIN SMALL LETTER S WITH ACUTE
  0x0179: 0x005a,     #  LATIN CAPITAL LETTER Z WITH ACUTE
  0x017a: 0x007a,     #  LATIN SMALL LETTER Z WITH ACUTE
  0x017b: 0x005a,     #  LATIN CAPITAL LETTER Z WITH DOT ABOVE
  0x017c: 0x007a,     #  LATIN SMALL LETTER Z WITH DOT ABOVE
  0x0230: 0x004f,     #  LATIN CAPITAL LETTER O WITH DOT ABOVE AND MACRON
# Greek letters, technical symbols and misc
  0x2190: 0x007f,     #  LEFTWARDS ARROW
  0x2192: 0x007e,     #  RIGHTWARDS ARROW

}
