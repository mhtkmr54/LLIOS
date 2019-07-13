import json

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
jsonstring = {}
jsonstring["type"] = "service_account"
jsonstring["project_id"] = "waorders"
jsonstring["private_key_id"] = "c3a5243ac27bd445c79b66e9e85bec1a3543dbab"
jsonstring["private_key"] = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQimnCLxOneXq2\nrfCilgUukl6KrPeYroJivuxJFjR1Wh9fZ4cnYTXx0hWtGorCpdNBS7Nbhi9Uxv3q\nnKGAD2BwYb+Phn4JxjGJfo3KCIgt7cElN45nRkfkX8Osu1NEkgV6ahrpWRhS+2MM\nexwhTl6d13uQsSZDqCEHRD2x1+PHy1K9plQX6vQPcDXeDUn/fDgH2OnN0aeEv7AY\n5YZYoCBw3i9WCnXcwHIU8A9Yuyli/URyDJUiPs8JlO5f9HtYTI5VUuM4gGARsilB\n3Dsfkq+EDmLiCP6BuIWGXdYixwAR+H3ItFlu/G+siRNmpTyfiWXxVr1zOKCjBpVF\nKzgk/x09AgMBAAECggEAMiLUwkanJwBhrEGtNKl0nXm7GQP0ktSBrFPSYs/f1MbR\n/BHbwG/ylCy54WAcNCfB3lTgzgQ4pN0idqEpgqwvt1UIxOzEqHzps/ClDgl3E/Ox\nF81/gvy2lAUh+gkfP8ELaB7SUX+GBY1ChuGiJa+9t5zyrBqq5GErb5/MZVFOBd5A\n8I1A6HPomy9CakIVfErEulOy+jbkR4rrRWDNajnl3sqf2ZsS7VeguDsUuUZPks3q\n9vJNzup/N24q/jUlnJJSp5blmx51e0cDTNAuflZjyhZzk7x5ITDl6E9Y0O5JSjhA\nrA52swmQfoJUArzt/TozQVls/FPuRzdNKm+Hp64R0QKBgQDn8CzyWn0FwX0Zmhk8\n5T4HNf9tZqwSLZXjTkbQQkKacxkSBZVLNQMzwhtbsPg3LHvzDUBGOSapWkutElrY\nwfzdlILHU1AY4XmQKpCNCn71BpcdNP+vJGF56DgvfWwRy1Rx8Mwr0q7epWaETx19\nMsRDx1E5q88hxMsuam4XjhowHwKBgQDmLNhwqQJJ06N4Ze+Bhyn2PrPmX1FIKA7I\nbqgGTVvlpaJNJN26ie6Jx9FvzH9G0C9V3TS8mIAZLNOU8MphohNkKZ5ObPQ3bqtl\nOx04/g5MtlyZSLBz/hhX9nMaIXAU7/uK1LyGO+q4/we93kIAHvj9D8EKisKvoBMq\ng7RRzPBXIwKBgGNLfmKO/MEvEbiZMT7RwZlis6SJdRcfLvEuPMDB7TOkHNKLU1vs\nKR/KdN3vSISOZc4rGR43L2cHQiipF/1+JxxRjR96emr8dIeUwWewW6PYm28klmXL\nxHNlSFCEeHSxwMg6153XR4gH9XilSjGkP0PpG8v90uJZFscbR2CMNIfvAoGAR1Bj\nqtwiUl9ZCYeDoj0PejTJJjooA9QtaFoogvNa4pbj50Th0dbEajnXoOzaDkWYNOE5\nYqlZHvOthjroaUF/AoyGeMP3EmmeftnG3w6PvaLOo8tKqFV0k2RPGyx6/nGwHL52\nvpw3yCNz8Za4GjN+b2F/LNX7JdDRv11Y8/MsD8MCgYBWniyxSjVTM1hPZczKnHs1\nCAGvCHfUdZxM/6ur2O8swV9T+rnFYpJoBhH3BCvf405reUKAlrDGPSq0cBp0/Yw8\nmue7gbTd08T8+6tGwo4p+XpZ83R7QysIQf9naGYCNAQdvQICLDMT6hClJj+Rrs1m\nSeaoN2OAWL3Hgoyu7oXfGg==\n-----END PRIVATE KEY-----\n"
jsonstring["client_email"] = "waordersservice@waorders.iam.gserviceaccount.com"
jsonstring["client_id"] = "118030233531111497520"
jsonstring["auth_uri"] = "https://accounts.google.com/o/oauth2/auth"
jsonstring["token_uri"] = "https://oauth2.googleapis.com/token"
jsonstring["auth_provider_x509_cert_url"] = "https://www.googleapis.com/oauth2/v1/certs"
jsonstring["client_x509_cert_url"] = "https://www.googleapis.com/robot/v1/metadata/x509/waordersservice%40waorders.iam.gserviceaccount.com"

with open('client_secret.json', 'w') as outfile:  
    json.dump(jsonstring, outfile)
