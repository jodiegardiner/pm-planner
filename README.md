# PM Planner
### A client relationship management tool for Private Midwives

[Live site](https://pm-planner.herokuapp.com)

## Technologies used
Djano back-end
MySQL database
JQuery
JQueryUI
Javascript
Bootstrap 4.0
FontAwesome
CSS3
AWS static/media storage and serve
Stripe payment system
Google OAuth2
Heroku deployment
Github repo



## 3rd-party utils
* Theme - [Dashgum admin theme](http://blacktie.co/2014/07/dashgum-free-dashboard/)
* [Datepicker js utility](https://jqueryui.com/datepicker/)
* [NiceScroll - attractive scroll bar](https://github.com/inuyaksa/jquery.nicescroll)
* [X-Editable - inline form editor](https://vitalets.github.io/x-editable/)
* [Gritter notifications](https://github.com/jboesch/Gritter)

## Rationale
My partner, a private homebirth midwife for a company called Private Midwives (Ireland), initially wanted a simple app to input a Due Date for a client and the app would create a number of Google Calendar entries to remind her to arrange various appointments, send various letters etc.  From there it grew into a fully fledged Customer Relationship Management application which is in the process of being tested "in the wild" and continues in development with a growing feature list for the future.

I wanted to create an app that would work across multiple platforms as her company's proprietary system can only be used from a desktop client which is proving largely useless for users who spend much of their time in the field.

I also wanted to keep things very simple as the intended user base are not necessarily tech-savvy, even tech-resistant in some cases, so it had to just work, in an obvious way without fuss or hassle.  Midwives have plenty enough of that.

## Features
Currently a user can register/login, create a client, manage existing clients, view and post to a forum, purchase supplies, or visit the Company's webportal or pricing page.

Technically speaking, the app can indeed be accessed from any device that has a browser and functions on all browsers identically. The accounts package has been modified so that Login is done using either the provided username or email address in combination with a password.

In terms of the models, there are currently two, Clients and Pregnancies. A single client may have multiple pregnancies of course, so it was important to separate these, whilst maintaining a link.

I wanted to keep the client creation form relatively simple. At a bare minimum, a user only needs to enter a Client's name to create a database entry.  If only a name is provided, a Pregnancy is still created in the database with no information logged in it beyond the link to the Client.  The Pregnancy can be updated at a later date using the inline editor. Most of the fields in the Client record are missing from the client creation form, quite deliberately.  This avoids having one huge sprawling form and given the way that the app is used, most of the details for a client will not be available anyway when the Client record is created.  All these fields are editable directly inline from a Client Detail page. Setting the code up to do this was important to my partner as it best facilitated the way the actual app would be used.

There are a long list of features planned for the future that utilise the Google OAuth code a lot more thoroughly.  
* Linking to google forms to mail merge the batch of letters that every new birth results in, for example. 
* Pull down updated Policy documents automatically and alert the midwife to changes to them. 
* Incorporation of an in-app calendar. 
* Ability for users to mark themselves available as "Seconds" for certain dates (Seconds are mandatory backup midwives who attend the birth with the primary midwife). 

My partner constantly thinks up new and useful features the app could have, and I have also compared what I have done closely to existing similar commerical products already out there. I have much still to do but already I think what I have created is comparable to some of what is commerically available.

The majority of all this organisation and paperwork is currently done by the midwives themselves, with virtually no systems in place with the Company, so there is a real desire to automate and simplify as much of this as possible, freeing up midwives for far more important uses of their time. I see this as a sort of desirable feature that isn't really a feature of the app itself but nevertheless results ina  lot of value to the Company.

## Theme/UX
I modified the Dashgum Admin theme quite extensively, incorporating the colour scheme from Private Midwives throughout, as well as using their logo.  It is a trivial matter to reskin the app for another client or for a more "general" theme without any company-specific identity. Something which may prove invaluable in future (it is literally as simple as mass find and replacing the hex values specified at the top of the custom.css file).

I kept images to an absolute minimum.  There is only one static image in fact, the primary logo that appears in the left-hand nav menu.  I used FontAwesome extensively throughout to add some visual flair despite the dearth of images. FontAwesome is so ubiquitous on the web now that pages without it just look a bit dated, to my eyes.  From a user's POV, they just expect it and, crucially, those icons are rather familar and easily recognisable.

Navigation is simple and can be toggled, and is hidden completely on smaller screen widths (though can of course be toggled back on there). In addition to that, I tried to put the most useful navigation elements in multiple locations that made sense.  For example, a user can add a client directly from the navigation menu, or from the menu that greets a user on login, or from the existing clients list (top and bottom). I tried to ensure that you would never need to click more than twice or scroll at all to get to the client creation form regardless of where you were on the site, and with the exception of an edge-case or two, I achieved that I believe.

If you do ever find yourself at the bottom of a very long page, and have the navigation hidden there is the ubiquitous "Back to top" button on the footer.

## Issues
Having your significant other as your client can mean shifting requirements! On this I shall say no more.

Users are so used to the invisible nature of development now that what they perceive as a trivial feature can mean many lines of code to write and a cascade of issues to tackle. "Can you just add feature X?" isn't always as straightforward as that. I discovered this many times over during the early development of the project but more acutely as I was approaching the submission deadline.  While I intend to continue developing this app for sale in the future, some features that I did considerable work on had to be stripped out or stripped back for the project submission deadline.

One of the big issues I overcame was making the details of every Model editable in-line. I used X-Editable for this and figuring out how that worked took me a long time.  It was crucial though, as the end result is a much cleaner experience for the user than having to go back to a dull form every time they want to update some information. It definitely felt like time well spent.

Initially I spent a lot of time getting the Google Calendar entries to work.  Which they did, flawlessly. When a Client was created with a due date provided, several calendar entries were generated and the dates for those were calculated from the combination of the Due Date and the Package of Care that a client had purchased. This was my crowning achievement for the time, really, and much celebration was had when it first worked. It was only after deployment to Heroku that I discovered the method I had been using to do that only worked from a command line and not from a web app.  This led me to having to learn about OAuth2 in more detail and in its current state, the app can authorise with Google, and store the credentials as a cookie on the users machine, but I haven't yet finished the code for actually using that authorisation to write events to the Calendar API.  I am close, very close, but it did not make it in to the final submission for the project deadline.  Which is highly disappointing to say the least. I have daily reminders from Google Calendars coming through from all the testing I did in those early efforts just to rub salt in that particular wound.

I have obviously chosen not to use the We Are Social app that was largely provided as is.  I did, however, incorporate a Forum with some rudimentary styling though this area was not really the focus of the app in the first place and I predict it would be used sparingly by users.  I would most likely cut it from any commerical release unless it proves in field testing to be something useful.  I mostly put it in to demonstrate I could do it.  The same can largely be said for the products and payment systems.  They are somewhat out of place in this kind of app and aren't realistically going to appear in a commercial version but again, proving I could understand the code behind it is important.  The products system did mean I had to use the MEDIA_URL and so on part of Django and AWS storage so it was absolutely not wasted time.  Those skills will be invaluable (and the code harvested) for future projects I am sure.

There are some security issues which require addressing before the app can be used to store real data in its current form.  Naturally, medical data is very sensitive so the database must be watertight. This can be achieved using one of the paid tiers of service that Heroku provide (or with a bit more advanced knowledge of AWS that I simply do not have yet). In terms of the front end, the commerical version would not permit Registration, users would be created by Admin and a more robust system would need to be in place to verify the user, perhaps even 2FA. As far as I could, I tried to ensure nothing is exposed to the browser that would offer a security vulnerability in terms of http responses, or Puts or anything of that ilk, though I have to confess to limited knowledge on what hackers are capable of and would seek advice before launching anything commerically.

## Code for the future
There is a "Pregnancy Events" model which is in preparation for a built-in calendar for the app.  A user will be able to request calendar events which will be calculated off the due date in a similar way to the Google Calendar events system, as well as being able to add individual events as required.  These events will be stored as Pregnancy Events and will provide a record of appointments made/kept for a given Pregnancy, a crucial part of this CRM's functionality which will cut Midwife admin time substantially. It will also provide the Company with a complete record in a single format which will greatly improve their accounting and reporting I would imagine. Down the line it might also be able to interface with their own systems in a useful fashion, further streamlining the process.


