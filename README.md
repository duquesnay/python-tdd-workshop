# Über currency extractor
Small code to be de-loaded on heroku, to format amount extracted from Über receipt
- split out even if there’s no space between the sign and the numbe
- turn currency sign into 3-letters currency
- provided as two services (currency, and amount), so works even if fields are separated already by uphill service (such as zapier email parser)

Included
- unit tests (can have a beat of BDD cleanup/restyled)
- couple of binaries to set up a new command line environment (creating virtual_env, running pip, etc)
- minimalist requirements
- heroku stuff to run on python 3