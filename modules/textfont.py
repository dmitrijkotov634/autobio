from typing import Union

from .utils import Cycle
from .value import Value


class TextFont(Value):
    pattern = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"

    _caps = {
        "typewriter": "𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕𝚣𝚡𝚌𝚟𝚋𝚗𝚖𝚀𝚆𝙴𝚁𝚃𝚈𝚄𝙸𝙾𝙿𝙰𝚂𝙳𝙵𝙶𝙷𝙹𝙺𝙻𝚉𝚇𝙲𝚅𝙱𝙽𝙼",
        "outline": "𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃ℤ𝕏ℂ𝕍𝔹ℕ𝕄",
        "serif_bold": "𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥𝐳𝐱𝐜𝐯𝐛𝐧𝐦𝐐𝐖𝐄𝐑𝐓𝐘𝐔𝐈𝐎𝐏𝐀𝐒𝐃𝐅𝐆𝐇𝐉𝐊𝐋𝐙𝐗𝐂𝐕𝐁𝐍𝐌",
        "serif_bold_italic":
        "𝒒𝒘𝒆𝒓𝒕𝒚𝒖𝒊𝒐𝒑𝒂𝒔𝒅𝒇𝒈𝒉𝒋𝒌𝒍𝒛𝒙𝒄𝒗𝒃𝒏𝒎𝑸𝑾𝑬𝑹𝑻𝒀𝑼𝑰𝑶𝑷𝑨𝑺𝑫𝑭𝑮𝑯𝑱𝑲𝑳𝒁𝑿𝑪𝑽𝑩𝑵𝑴",
        "serif_italic": "𝑞𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝𝑎𝑠𝑑𝑓𝑔ℎ𝑗𝑘𝑙𝑧𝑥𝑐𝑣𝑏𝑛𝑚𝑄𝑊𝐸𝑅𝑇𝑌𝑈𝐼𝑂𝑃𝐴𝑆𝐷𝐹𝐺𝐻𝐽𝐾𝐿𝑍𝑋𝐶𝑉𝐵𝑁𝑀",
        "small_caps": "ǫᴡᴇʀᴛʏᴜɪᴏᴘᴀsᴅғɢʜᴊᴋʟᴢxᴄᴠʙɴᴍQWERTYUIOPASDFGHJKLZXCVBNM",
        "script": "𝓆𝓌ℯ𝓇𝓉𝓎𝓊𝒾ℴ𝓅𝒶𝓈𝒹𝒻ℊ𝒽𝒿𝓀𝓁𝓏𝓍𝒸𝓋𝒷𝓃𝓂𝒬𝒲ℰℛ𝒯𝒴𝒰ℐ𝒪𝒫𝒜𝒮𝒟ℱ𝒢ℋ𝒥𝒦ℒ𝒵𝒳𝒞𝒱ℬ𝒩ℳ",
        "script_bold": "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶𝓠𝓦𝓔𝓡𝓣𝓨𝓤𝓘𝓞𝓟𝓐𝓢𝓓𝓕𝓖𝓗𝓙𝓚𝓛𝓩𝓧𝓒𝓥𝓑𝓝𝓜",
        "sans_bold": "𝗾𝘄𝗲𝗿𝘁𝘆𝘂𝗶𝗼𝗽𝗮𝘀𝗱𝗳𝗴𝗵𝗷𝗸𝗹𝘇𝘅𝗰𝘃𝗯𝗻𝗺𝗤𝗪𝗘𝗥𝗧𝗬𝗨𝗜𝗢𝗣𝗔𝗦𝗗𝗙𝗚𝗛𝗝𝗞𝗟𝗭𝗫𝗖𝗩𝗕𝗡𝗠",
        "sans_bold_italic":
        "𝙦𝙬𝙚𝙧𝙩𝙮𝙪𝙞𝙤𝙥𝙖𝙨𝙙𝙛𝙜𝙝𝙟𝙠𝙡𝙯𝙭𝙘𝙫𝙗𝙣𝙢𝙌𝙒𝙀𝙍𝙏𝙔𝙐𝙄𝙊𝙋𝘼𝙎𝘿𝙁𝙂𝙃𝙅𝙆𝙇𝙕𝙓𝘾𝙑𝘽𝙉𝙈",
        "sans_italic": "𝘲𝘸𝘦𝘳𝘵𝘺𝘶𝘪𝘰𝘱𝘢𝘴𝘥𝘧𝘨𝘩𝘫𝘬𝘭𝘻𝘹𝘤𝘷𝘣𝘯𝘮𝘘𝘞𝘌𝘙𝘛𝘠𝘜𝘐𝘖𝘗𝘈𝘚𝘋𝘍𝘎𝘏𝘑𝘒𝘓𝘡𝘟𝘊𝘝𝘉𝘕𝘔",
        "sans": "𝗊𝗐𝖾𝗋𝗍𝗒𝗎𝗂𝗈𝗉𝖺𝗌𝖽𝖿𝗀𝗁𝗃𝗄𝗅𝗓𝗑𝖼𝗏𝖻𝗇𝗆𝖰𝖶𝖤𝖱𝖳𝖸𝖴𝖨𝖮𝖯𝖠𝖲𝖣𝖥𝖦𝖧𝖩𝖪𝖫𝖹𝖷𝖢𝖵𝖡𝖭𝖬",
        "gothic": "𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏ℨ𝔛ℭ𝔙𝔅𝔑𝔐",
        "gothic_bold": "𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒𝕼𝖂𝕰𝕽𝕿𝖄𝖀𝕴𝕺𝕻𝕬𝕾𝕯𝕱𝕲𝕳𝕵𝕶𝕷𝖅𝖃𝕮𝖁𝕭𝕹𝕸",
    }

    _numbers = {
        "circles":
        "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ🄋➀➁➂➃➄➅➆➇➈",
    }

    _fonts = {
        "tiny": "ᵠʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ",
        "comic": "ᑫᗯᗴᖇTYᑌIOᑭᗩՏᗪᖴᘜᕼᒍKᒪᘔ᙭ᑕᐯᗷᑎᗰ",
        "circles_black": "🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜",
        "squares": "🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼",
        "squares_black": "🆀🆆🅴🆁🆃🆈🆄🅸🅾🅿🅰🆂🅳🅵🅶🅷🅹🅺🅻🆉🆇🅲🆅🅱🅽🅼",
        "manga": "Ҩ山乇尺ㄒㄚㄩ|ㄖ卩卂丂ᗪ千ᘜ卄ﾌҜㄥ乙乂匚ᐯ乃几爪",
        **_caps,
        **_numbers
    }

    def caps():
        return Cycle(*_caps.keys())

    def numbers():
        return "circles"  # Cycle(*_numbers.keys())

    def fonts():
        return Cycle(*_fonts.keys())

    def __init__(self, text: Union[Value, str], font: Union[Value, str]):
        """Applies a text font to a string

        :param text: Text
        :param font: Text font name
        """
        self.text = text
        self.font = font

    async def get(self, **data) -> str:
        font = self._fonts[await Value.resolve(self.font, **data)]
        result = []
        for c in await Value.resolve(self.text, **data):
            if c not in self.pattern:
                result += c
                continue
            i = self.pattern.index(c)
            result.append(font[i] if i < len(font) else c)
        return "".join(result)
