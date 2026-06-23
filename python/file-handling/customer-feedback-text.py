feedback_text = """Customer Feedback Report - January 2024
===============================================

Customer: Alaje Timothy O. - Rating: 4/5
Comment: Great food but delivery was 15 minutes late.
Date: 2024-01-15

Customer: Keziah Tanko W. - Rating: 5/5
Comment: Absolutely amazing experience! Will order again.
Date: 2024-01-16

Customer: Aliyu J. - Rating: 2/5
Comment: Food was cold when it arrived. Disappointed.
Date: 2024-01-16

Customer: Abbas N. - Rating: 5/5
Comment: Best pizza in town! Quick delivery too.
Date: 2024-01-17

Customer: Michael T. - Rating: 3/5
Comment: Decent food but overpriced for the portion size.
Date: 2024-01-18

Customer: Madinato R. - Rating: 4/5
Comment: Good variety on the menu. Friendly delivery person.
Date: 2024-01-19

Customer: Daniel P. - Rating: 1/5
Comment: Wrong order delivered. Customer service unhelpful.
Date: 2024-01-19

Summary Statistics:
Average Rating: 3.4/5
Total Reviews: 7
Positive Reviews (4-5 stars): 4
Negative Reviews (1-2 stars): 2
"""

with open("customer_feedback.txt", "w") as f:
    f.write(feedback_text)