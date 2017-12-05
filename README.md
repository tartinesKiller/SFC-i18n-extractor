# SFC-i18n-extractor
Simple Python script to extract i18n blocks from vuejs's single file component, in order to put them all in a single json.

# Usage
```bash
python3 main.py path/to/src/folder > path/to/translations.json
```

# Example
If both Hello.vue and Cheese.vue contains translations blocks like so:
```html
...
</template>
<i18n>
{
    "en": {
        "hello": "Hello!"
    },
    "fr": {
        "hello": "Bonjour !"
    }
}
</i18n>
<script>
...
```
It will be converted like that: 
```json
{
    "en": {
        "Hello.vue": {
            "hello": "Hello!"
        },
        "Cheese.vue": {
            ...
        }        
    },
    "fr": {
        "Hello.vue": {
            "hello": "Bonjour !"
        },
        "Cheese.vue": {
            ...
        }        
    }
}
```
