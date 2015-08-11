# obliques
Sends an SMS via Twilio with one of Brian Eno's Oblique Strategies in it.
By default, it sends an SMS at a random time between 10:00 and 20:00 system time, but you can do it however you like.

### Dependencies:
- this cron job: 0 0 * * * <path-to-script>
- this env var: OBLIQUES_CONF_ABS_PATH=/absolute/path/to/script (this is because cron's working directory isn't where the script is run from so it loses the conf file)

### TODO:
- remove dependence on midnight cron job
- allow multiple recipients
- make time randomisation smarter
