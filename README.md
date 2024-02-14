# Data Engineer Coding Exercise

Hi there!

If you're reading this, it means you're now at the coding exercise step of the data-engineering hiring process. 
We're really happy that you made it here and super appreciative of your time!

This repo is intentionally left empty except for the file you are currently reading. Please add your work with as much 
detail as you see fit.

## Expectations

* It should be executable, production ready code
* Take whatever time you need - we won’t look at start/end dates, you have a life besides this, and we respect that! 
Moreover, if there is something you had to leave incomplete or there is a better solution you would implement but 
couldn't due to personal time constraints, please try to walk us through your thought process or any missing parts, 
using the “Implementation Details” section below.

## About the Challenge

The goal of this exercise is for you to implement a fully functional end-to-end ETL pipeline via the open-source, 
full-stack data integration platform [Meltano](https://meltano.com/).

You will be working with the data provided by the [SpaceX API](https://github.com/r-spacex/SpaceX-API/tree/master), and
as it should be with any good data challenge, your work will be guided by one central question that we are aiming to
help find an answer for:

> When will there be 42,000 Starlink satellites in orbit, and how many launches will it take to get there?

You can assume that you will have a team of Data Analysts working in collaboration with you so you do not have to
provide the full solution. However, in your role as a Data Engineer, we would expect you to:

* create a Meltano custom extractor for [SpaceX-API](https://github.com/r-spacex/SpaceX-API/blob/master/docs/README.md) 
(following [this official tutorial](https://docs.meltano.com/tutorials/custom-extractor))
* configure Meltano`s [target-postgres](https://hub.meltano.com/loaders/target-postgres/) loader to send the data
extracted from the source by your custom extractor in the previous step into [Postgres](https://www.postgresql.org/)
* add a data transformation step via [Meltano`s implementation of dbt](https://docs.meltano.com/guide/transformation). 
Specifically:
  * Add a data transformation step via Meltano’s implementation of dbt. It must include a `transformation_updated_at` timestamp. This should result in a model (or models) that can be handed off to a team of data analysts.
* configure a [job](https://docs.meltano.com/reference/command-line-interface#job) in your Meltano project that runs the 
previous 3 steps in sequence

### When you are done

* Complete the "Implementation Details" section at the bottom of this README.
* Open a Pull Request in this repo and send the link to the recruiter with whom you have been in touch.
* You can also send some feedback about this exercise. Was it too short/big? Boring? Let us know!

## Useful Resources

* [Meltano Official Website](https://meltano.com/)
* [Meltano Docs](https://docs.meltano.com/)
* [Meltano Tutorial: Create a Custom Extractor](https://docs.meltano.com/tutorials/custom-extractor)
* [Meltano target-postgres Docs](https://hub.meltano.com/loaders/target-postgres/)
* [SpaceX-API Docs](https://github.com/r-spacex/SpaceX-API/blob/master/docs/README.md)
* [dbt Docs](https://docs.getdbt.com/)

## Implementation Details

This section is for you to fill in with any decisions you made that may be relevant. You can also change this README to 
fit your needs.
