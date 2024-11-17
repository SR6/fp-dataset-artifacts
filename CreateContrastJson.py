import json

data = [
    {"premise": "A man selling donuts to a customer during a world exhibition event held in the city of Angeles", "hypothesis": "A man selling donuts to a customer.", "label": 0},
    {"premise": "A man selling donuts to a dog during a world exhibition event held in the city of Angeles", "hypothesis": "A man selling donuts to a customer.", "label": 1},
    {"premise": "A man in a green jersey and rollerskates stumbles as a man in a black jersey appears to collide with him.", "hypothesis": "They both fall to the ground.", "label": 1},
    {"premise": "A man in a green jersey and rollerskates stumbles as a man in a black jersey appears to collide with him.", "hypothesis": "The man falls to the ground.", "label": 0},
    {"premise": "A taxi SUV drives past an urban construction site, as a man walks down the street in the other direction.", "hypothesis": "A man is chasing an SUV that is going in the same direction as him.", "label": 2},
    {"premise": "A taxi SUV drives past an urban construction site, as a man walks down the street in the other direction.", "hypothesis": "A man is not chasing an SUV.", "label": 0},
    {"premise": "A taxi SUV drives past an urban construction site, as a man walks down the street in the other direction.", "hypothesis": "A man is chasing an SUV that is going in the opposite direction as him.", "label": 1},
    {"premise": "A woman is talking on the phone while standing next to a dog.", "hypothesis": "A woman is walking her dog.", "label": 1},
    {"premise": "A woman is talking on the phone while standing next to a dog.", "hypothesis": "A woman is walking her horse.", "label": 2},
    {"premise": "A small ice cream stand with two people standing near it.", "hypothesis": "Two people selling ice cream from a car.", "label": 2},
    {"premise": "A small ice cream stand with two people standing near it.", "hypothesis": "Two people selling ice cream from a stand.", "label": 0},
    {"premise": "Number 916 is hoping that he is going to win the race.", "hypothesis": "A person is betting that he will win  the race.", "label": 1},
    {"premise": "Number 916 is hoping that he is going to win the race.", "hypothesis": "A person is wishing that he will win  the race.", "label": 0},
    {"premise": "A man waterskies with a life jacket.", "hypothesis": "A lifeguard races across the water.", "label": 1},
    {"premise": "A man waterskies with a life jacket.", "hypothesis": "A man races across the water.", "label": 0},
    {"premise": "A man poses for a photo in front of a Chinese building by jumping.", "hypothesis": "The man has experience in taking photos.", "label": 1},
    {"premise": "A man poses for a photo in front of a Chinese building by jumping.", "hypothesis": "The man hates being in photos.", "label": 2},
    {"premise": "A boy looks surly as his father looks at the camera.", "hypothesis": "a younger boy looks at his father", "label": 1},
    {"premise": "A boy looks surly as his father looks at the camera.", "hypothesis": "a younger boy looks at his mother", "label": 2},
    {"premise": "A man with a white towel wrapped around the lower part of his face and neck.", "hypothesis": "He doesn't want hair to land on his neck.", "label": 1},
    {"premise": "A man with a white towel wrapped around the lower part of his face and neck.", "hypothesis": "He doesn't want hair to land on his mouth.", "label": 0},
    {"premise": "a little girl sitting in a seat.", "hypothesis": "She is in a chair.", "label": 1},
    {"premise": "a little girl sitting in a seat.", "hypothesis": "A boy is in a chair.", "label": 2},
    {"premise": "Nine women in white robes with hoods walk on plush, green grass.", "hypothesis": "The women are wearing flip flops.", "label": 1},
    {"premise": "Nine women in white robes with hoods walk on plush, green grass.", "hypothesis": "The women are wearing robes.", "label": 0},
    {"premise": "A man is holding a both a sleeping toddler and a sleeping baby on his lap.", "hypothesis": "A toddler and baby play together while their father looks on.", "label": 2},
    {"premise": "A man is holding a both a sleeping toddler and a sleeping baby on his lap.", "hypothesis": "A toddler and baby sleep together while their father looks on.", "label": 0},
    {"premise": "A woman rock-climbs in a rural area.", "hypothesis": "The woman is exercising.", "label": 1},
    {"premise": "A woman rock-climbs in a rural area.", "hypothesis": "The woman is sleeping.", "label": 2},
    {"premise": "A woman rock-climbs in a rural area.", "hypothesis": "The woman is climbing.", "label": 0},
    {"premise": "An older woman on the computer", "hypothesis": "Woman using her personal computer.", "label": 1},
    {"premise": "An older woman on the computer", "hypothesis": "Woman using her computer.", "label": 0},
    {"premise": "A woman in a gray shirt working on papers at her desk.", "hypothesis": "Lady showing result of anger on her boss scolding", "label": 2},
    {"premise": "A woman in a gray shirt working on papers at her desk.", "hypothesis": "Lady showing improvement on her boss scolding", "label": 1},
    {"premise": "A woman is holding a sign that says honk to indict bush.", "hypothesis": "The woman has a mullet.", "label": 2},
    {"premise": "A woman is holding a sign that says honk to indict bush.", "hypothesis": "The woman has a sign.", "label": 0},
    {"premise": "A man in a tank top holds a metal bar against a wall.", "hypothesis": "The man is demolishing a house.", "label": 1},
    {"premise": "A man in a tank top holds a metal bar against a wall.", "hypothesis": "The man is hitting a house.", "label": 1},
    {"premise": "A greyhound jumps over a chain.", "hypothesis": "A dog ran away from the racetrack.", "label": 1},
    {"premise": "A greyhound jumps over a chain.", "hypothesis": "A dog ran at the racetrack.", "label": 1},
    {"premise": "A greyhound jumps over a chain.", "hypothesis": "A horse ran away from the racetrack.", "label": 2},
    {"premise": "A young boy is taking a nap underneath a piece of cardboard that reads, \"Connie Facial Tissues.\"", "hypothesis": "He sleeps under a large blanket", "label": 2},
    {"premise": "A young boy is taking a nap underneath a piece of cardboard that reads, \"Connie Facial Tissues.\"", "hypothesis": "He sleeps under a structure", "label": 1},

]

with open('contrast_data.jsonl', 'w') as f:
    for item in data:
        json.dump(item, f)
        f.write('\n')