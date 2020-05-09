from constants import Direction
raw_words = [
  {
    "q": "שם חיבה ליובל",
    "ans": "יושקין",
    "start_row": 0,
    "start_col": 0,
    "direction": Direction.horizontal
  },
  {
    "q": "מכינוייו האופנתיים של אבא בארמית",
    "ans": "שיקין",
    "start_row": 0,
    "start_col": 11,
    "direction": Direction.horizontal
  },
  {
    "q": "שם חיבה לכולם",
    "ans": "פושקינים",
    "start_row": 2,
    "start_col": 5,
    "direction": Direction.horizontal
  },
  {
    "q": "שם חיבה נוסף ליובל",
    "ans": "יוש",
    "start_row": 11,
    "start_col": 4,
    "direction": Direction.vertical
  },
  {
    "q":"בהישג יד" ,
    "ans": "בשלוף",
    "start_row": 1,
    "start_col": 10,
    "direction": Direction.vertical
  },
  {
    "q": "ברכת בוקר נעימה",
    "ans": "יום מלבלב",
    "start_row": 0,
    "start_col": 5,
    "direction": Direction.vertical
  },
  {
    "q": "אוכל טעים",
    "ans": "הכי טעים בעולם",
    "start_row": 12,
    "start_col": 2,
    "direction": Direction.horizontal
  },
  {
    "q": "לילה טוב",
    "ans": "נימבוס אלפים",
    "start_row": 2,
    "start_col": 7,
    "direction": Direction.vertical
  },
  {
    "q": "מי שמשועמם",
    "ans": "מטומטם",
    "start_row": 4,
    "start_col": 7,
    "direction": Direction.horizontal
  },
  {
    "q": "תחום במתמטיקה",
    "ans": "אקטואריה",
    "start_row": 5,
    "start_col": 13,
    "direction": Direction.vertical
  },
  {
    "q": "זמר דומה לבעלך",
    "ans": "מתי כספי",
    "start_row": 6,
    "start_col": 11,
    "direction": Direction.vertical
  },
  {
    "q": "יוצרת שקשוקה מפורסמת",
    "ans": "רינה",
    "start_row": 11,
    "start_col": 8,
    "direction": Direction.vertical
  },
  {
    "q": "ערך הדיון הרטוב בפיניין עברי",
    "ans": "שווי",
    "start_row": 3,
    "start_col": 12,
    "direction": Direction.horizontal
  },
  {
    "q": "משתמש באובניים",
    "ans": "קדר",
    "start_row": 3,
    "start_col": 0,
    "direction": Direction.horizontal
  },
  {
    "q": "מתי ניפגש כולנו",
    "ans": "בהקדם",
    "start_row": 6,
    "start_col": 11,
    "direction": Direction.horizontal
  },
  {
    "q": "לאן נסעה משפחת קובלנץ",
    "ans": "ארצה",
    "start_row": 6,
    "start_col": 0,
    "direction": Direction.horizontal
  },
  {
    "q": "אירוע ראוי ליום זה",
    "ans": "מסיבה",
    "start_row": 7,
    "start_col": 4,
    "direction": Direction.horizontal
  },
  {
    "q": "תחביב מנומס",
    "ans": "גינון",
    "start_row": 8,
    "start_col": 0,
    "direction": Direction.horizontal
  },
  {
    "q": "פיאנס בעברית",
    "ans": "חלב",
    "start_row": 9,
    "start_col": 6,
    "direction": Direction.horizontal
  },
  {
    "q": "יש קצינים עם פלאפל ויש קצינים ...",
    "ans": "עם אבכ",
    "start_row": 9,
    "start_col": 11,
    "direction": Direction.horizontal
  },
  {
    "q": "סוג מאכלים הכולל תפוח, בננה, אגס וכן הלאה",
    "ans": "פרי",
    "start_row": 11,
    "start_col": 7,
    "direction": Direction.horizontal
  },
  {
    "q": "מה שיש לנינו של האל איבד מטוס",
    "ans": "סבנה",
    "start_row": 14,
    "start_col": 8,
    "direction": Direction.horizontal
  },
  {
    "q": "המועדון שלך",
    "ans": "ספר",
    "start_row": 15,
    "start_col": 13,
    "direction": Direction.horizontal
  },
  {
    "q": "מזל ושנה",
    "ans": "שור וארנב",
    "start_row": 15,
    "start_col": 0,
    "direction": Direction.horizontal
  },
  {
    "q": "מורה ביסודי",
    "ans": "יהודית צדוק",
    "start_row": 0,
    "start_col": 1,
    "direction": Direction.vertical
  },
  {
    "q": "איך נוסעים לקפלן כשהאף מדמם",
    "ans": "יחפים",
    "start_row": 0,
    "start_col": 12,
    "direction": Direction.vertical
  },
  {
    "q": "שם חיבה לעמית",
    "ans": "עמיתוחס",
    "start_row": 9,
    "start_col": 15,
    "direction": Direction.vertical
  },
  {
    "q": 'יוצרי התשבץ בפעולה חשבונית (ר"ת)',
    "ans": "יפע",
    "start_row": 10,
    "start_col": 9,
    "direction": Direction.vertical
  },
  {
    "q": "זמר שלא דומה לאבא",
    "ans": "שלמה בר",
    "start_row": 10,
    "start_col": 2,
    "direction": Direction.vertical
  },
  {
    "q": "ענק שלג אגדי מההימלאיה",
    "ans": "יטי",
    "start_row": 11,
    "start_col": 13,
    "direction": Direction.horizontal
  },
  {
    "q": "איכותו של אדון צרפתי",
    "ans": "טיבו",
    "start_row": 12,
    "start_col": 10,
    "direction": Direction.vertical
  },
  {
    "q": "המציא את הגלגל של אמא",
    "ans": "הגה",
    "start_row": 7,
    "start_col": 4,
    "direction": Direction.vertical
  }
]


unused_words = [
  {
    "q": "",
    "ans": "",
    "start_row": 0,
    "start_col": 0,
    "direction": Direction.vertical
  },
  {
    "q": "שם השכונה של יובל",
    "ans": "פיצוחים",
    "start_row": 7,
    "start_col": 11,
    "direction": Direction.vertical
  }
]

  # {
  #   "q": "",
  #   "ans": "",
  #   "start_row": 0,
  #   "start_col": 0,
  #   "direction": Direction.
  # },

def process(text):
  changes = {" ": "", "ם": "מ", "ך": "כ", "ף": "פ", "ץ": "צ", "ן": "נ"}
  for old, new in changes.items():
    text = text.replace(old, new)
  return text

words = []
for word in raw_words:
  word['ans'] = process(word['ans'])
  words.append(word)