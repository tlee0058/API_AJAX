Ajax Pagination
Create using Ajax the application shown below. As the name gets changed, or as you update the from/to date, or as you update the page number, your application should update the table with the appropriate lead information

This is a GREAT assignment where you’ll learn a lot and this assignment could be added to your portfolio.

Some of our students have shown this assignment to potential employers and they were genuinely impressed by the fact that the students could build something like this all from scratch.

![alt tag](https://user-images.githubusercontent.com/32435667/38463792-67a0fc9c-3ad0-11e8-8284-d476876e299e.png)

Figuring out the ORM calls to make this work is great practice. Filtering, excluding and limits, oh yay, all combined with AJAX!

When you see this, do you see any form? You don’t because there is no submit button? Well. In Ajax, you don’t need to submit the form just with the submit button and in fact, a lot of Ajax forms do NOT have a submit button. So looking at the wireframe above, what information should be captured inside the form which you will be sending to another URL? Spend a few minutes and think about this.

Answer: basically, you want to include all information necessary for generating that table.

Now you may be thinking but page numbers are links not drop-down or input type text. Well. Looks can be deceiving. You could still make the page numbers look like links but may be you can use jQuery to update the value of the page number in the form when those links are clicked, ultimately resulting in the form having a hidden page number that can be submitted via AJAX.