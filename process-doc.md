06.10.2023

## Beautiful Soup

The first step is to get the parser Beautiful Soup to work. To reduce variables (i.e. things that can go wrong), use a manually copy-pasted sample of the HTML of the track listing for Please Please Me from wikipedia (instead of coding to visit the website directly) obtained from `https://en.wikipedia.org/wiki/Please_Please_Me#Track_listing`.

The following code tests that the parser is correctly installed (on our miniconda) and works. Our first task is to 'pretty print' it, so that the jumble of HTML comes out structured:

```
import bs4
exfile = open('beatles-track-listing.html')
exsoup = bs4.BeautifulSoup(exfile,'html.parser')
print(exsoup.prettify())
```

Observations from the pretty-print:

* The track listing section is has an `<h2>` with text 'Track listing', inside a `<span` with id `Track_listing`
* Each track title is preceded by the track number inside a `<th id="track2" scope="row">`
* There are two sides to the LP. Each has its own `<div class="track-listing">`

So for each album:
* Go to the 'Track listing' `<h2>` (might be unnecessary?)
* Look for the `<div class="track-listing">`
* Inside this `div`, look for a `<th` with id `track#`
* Extract the text of the `<td` right next to it.

Disadvantage of this is that we don't get the track order. Perhaps we don't need that anyway for this analysis.

Another thing to look at is that non-Lennon McCartney tracks are labelled within brackets. And that's not the only thing inside brackets e.g. Side One track 3 "Anna (Go to Him)" (Arthur Alexander)

One approach could be to look for the first `<a` inside the `<td` next to a `<th` that has an id `track#`, that is inside a `<div class="track-listing">`.

Hopefully all Beatles songs have been extensively researched and documented, such that each song has it's own `<a`.

BS experiment to do:

Download `https://en.wikipedia.org/wiki/Please_Please_Me#Track_listing` then retrieve all the `<div class="track-listing"` and print the contents.

Reading to do:
* https://proxyway.com/knowledge-base/how-to-get-text-from-div-using-beautifulsoup
* https://stackoverflow.com/questions/2136267/beautiful-soup-and-extracting-a-div-and-its-contents-by-id
