# Style Guide

<!-- omit in toc -->
## Table of contents
- [Acronyms](#acronyms)
- [Capitalization](#capitalization)
- [Developer content](#developer-content)
  - [Reference documentation](#reference-documentation)
  - [Code examples](#code-examples)
  - [Text formatting](#text-formatting)
- [Final publishing review](#final-publishing-review)
- [Global communication](#global-communication)
- [Grammar](#grammar)
  - [Verbs](#verbs)
    - [Verb tense](#verb-tense)
    - [Moods of verb](#moods-of-verb)
    - [Active and passive voice](#active-and-passive-voice)
    - [Verb agreements](#verb-agreements)
  - [Nouns and pronouns](#nouns-and-pronouns)
- [Unbiased communication](#unbiased-communication)

## Acronyms

- Do not create acronyms for brand, product, or feature names.
- Only use acronyms that the audience is familiar with.
- If you have to use an acronym, provide its expansion on first use.
- Do not introduce acronyms that are used just once.
- Avoid using acronyms in titles and headings.
- Lowercase all words in the spelled-out form of an acronym except for proper nouns.
- Add lowercase 's' to make an acronym plural. If the acronym stands for a plural noun, do not add an 's'.
- Avoid the possessive form unless an acronym refers to a person or an organization.

## Capitalization

- Use sentence-style capitalization; that means everything is lowercase except the first word of a sentence, heading, title, UI label, standalone phrase, and proper nouns.
- Always capitalize the first word of a new sentence. Transform sentences that starts with a word that is always lowercase.
- Do not use all uppercase for emphasis; instead use italic typeface.
- For design element, do not all lowercase; although all uppercase is used occasionally.
- Do not use internal capitalization unless it is part of a brand name.
- Do not capitalize the spelled-out form of an acronym unless it is a proper noun.
- When words are joined by a slash, capitalize the word after the slash if the word before the slash is capitalized.
- If a title or heading includes a colon, capitalize the first word after it.
- In programming languages, follow the traditional capitalization of keywords and other special terms.

## Developer content

### Reference documentation

| Section                      | Description                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Title and description**    | In title, use the name of a programming element followed by the element type. If the name is shared by multiple elements, add a differentiator or category in parenthesis. Provide concise sentences describing the element. If possible, explain what the element does or represents without repeating the element name.   |
| **Declaration / syntax**     | The code signature that defines the element. This section might also provide usage syntax. If the technology can be used with multiple programming languages, provide syntax for each language.                                                                                                                             |
| **Parameters**               | If the element has parameters, provide a description of each parameter and its data type. If appropriate, indicate whether the parameter is required or optional and whether it represents input or output. Provide as much useful detail as possible. Do not just repeat the words in the parameter name or the data type. |
| **Property value**           | A description of the value for a property or field. If the property or field has a default value, describe that as well. Include the data type of the property value is applicable.                                                                                                                                         |
| **Return value**             | If the element returns a value, describe the value and information about its data type. If the value is a Boolean that indicates the presence of a condition, describe the condition.                                                                                                                                       |
| **Exceptions / error codes** | If the element can throw exceptions or raise error codes, when called, list them and describe the conditions under which they occur.                                                                                                                                                                                        |
| **Remarks**                  | Additional information about the element and important details that may not be obvious from its syntax, parameters, or return value. It might explain what the element does in more detail, compare it with similar elements, and identify potential issues in its use.                                                     |
| **Example**                  | A code example that illustrates how to use the programming element.                                                                                                                                                                                                                                                         |
| **Requirements**             | Languages or platform requirements for using the element.                                                                                                                                                                                                                                                                   |
| **Permissions**              | Security permissions that apply to the element, if required.                                                                                                                                                                                                                                                                |
| **See also**                 | References or links to more information about element usage, related elements, or other relevant articles.                                                                                                                                                                                                                  |

### Code examples

- Create concise examples that exemplify key development tasks. Start with simple examples and build up complexity after you cover common scenarios.
- Prioritize frequently used elements and elements that may be difficult to use or understand.
- Do not use code examples to illustrate obvious points or fictitious scenarios.
- Create code examples that are easy to scan and understand. Reserve complicated examples for tutorials or walkthroughs, where you can provide a stepwise explanation of how the example works.
- Add an introduction to describe the scenario and explain anything that might not be obvious from the code. List the requirements and dependencies for using or running the example.
- Provide an easy way for developers to copy or run the code. If the code example demonstrates interactive or animated features, consider providing a way to the developers to run the example directly from your content page.
- Use appropriate keywords, linking strategies, and other search engine optimization (SEO) techniques to improve the visibility and usability of the code examples.
- Design code for reuse. Help developers determine what to modify. Add comments to explain details, but do not overdo by stating the obvious things.
- Show expected output, either in a separate section after the code example or by using code comments within the code example.
- Consider accessibility requirements for code that creates user interface.
- Write secure code; always validate user input, never hard-code passwords in code, and use code analysis tools to detect security issues.
- Show exception handling only when it is intrinsic to the example. Do not catch exceptions thrown when invalid arguments are passed to parameters.
- Always compile and test your code before providing them as examples.

### Text formatting

| **Element**                 | **Typeface** | **Case**       | **Separation** | **Example**                |
| --------------------------- | ------------ | -------------- | -------------- | -------------------------- |
| **Attributes**              | Bold         | Lowercase      | None           | **`href`**                 |
| **Classes**                 | Bold         | Pascalcase     | None           | **`LinkedList`**           |
| **Code samples**            | Regular      | None           | None           | `int main() { return 0; }` |
| **Command-line commands**   | Bold         | Lowercase      | None           | **`mkdir`**                |
| **Command-line options**    | Bold         | None           | None           | **`--verbose`**            |
| **Constants**               | Bold         | Uppercase      | Underscore     | **`INT_MAX`**              |
| **Control classes**         | Bold         | Uppercase      | None           | **`EDIT`**                 |
| **Data formats**            | Bold         | Uppercase      | Underscore     | **`LOCALE`**               |
| **Data structures**         | Bold         | None           | None           | **`stack`**                |
| **Data types**              | Bold         | Lowercase      | None           | **`float`**                |
| **Database names**          | Bold         | None           | None           | **`SQLite`**               |
| **Directives**              | Bold         | None           | None           | **`#include`**             |
| **Environment variables**   | Regular      | Uppercase      | None           | `NDEBUG`                   |
| **Error messages**          | Regular      | Sentence-style | None           | *Syntax error*             |
| **Event names**             | Bold         | None           | None           | **`OnClick`**              |
| **Fields**                  | Bold         | None           | None           | **`biPlanes`**             |
| **File attributes**         | Regular      | Lowercase      | None           | **`attrib`**               |
| **File extensions**         | Regular      | Lowercase      | None           | `.txt`                     |
| **File names**              | Regular      | Lowercase      | Hyphen         | `article-condensed.txt`    |
| **Folder names**            | Regular      | Lowercase      | Hyphen         | `/home/user/my-documents/` |
| **Functions**               | Bold         | Camelcase      | None           | **`printError()`**         |
| **Handles**                 | Regular      | Uppercase      | None           | `HWND`                     |
| **Keywords**                | Bold         | Lowercase      | None           | **`break`**                |
| **Logical operators**       | Bold         | Uppercase      | None           | **`AND`**                  |
| **Macros**                  | Bold         | Uppercase      | None           | **`IFDEF`**                |
| **Markup elements**         | Bold         | Lowercase      | None           | **`<body>`**               |
| **Mathematical constants**  | Italic       | Uppercase      | None           | *`PI`*                     |
| **Members**                 | Bold         | Camelcase      | None           | **`currentSize`**          |
| **Methods**                 | Bold         | Camelcase      | None           | **`getPrevious()`**        |
| **Operators**               | Bold         | None           | None           | **`+`**                    |
| **Parameters**              | Italic       | Lowercase      | None           | *`source`*                 |
| **Placeholders**            | Italic       | None           | None           | *`Password`*               |
| **Ports**                   | Regular      | Uppercase      | None           | `LPT1`                     |
| **Products and trademarks** | Regular      | Title-style    | None           | Mozilla Firefox            |
| **Properties**              | Bold         | Lowercase      | None           | **`font-weight`**          |
| **Registers**               | Regular      | Uppercase      | None           | `DS`                       |
| **Registry settings**       | Bold         | Uppercase      | None           | **`HKEY_CLASSES_ROOT`**    |
| **Statements**              | Bold         | None           | None           | **`IMPORTS`**              |
| **Structures**              | Bold         | None           | None           | **`ACCESSTIMEOUT`**        |
| **Switches**                | Bold         | Lowercase      | None           | **`build: commands`**      |
| **UI text**                 | Regular      | Sentence-style | None           | Report a bug?              |
| **URLs**                    | Regular      | Lowercase      | None           | `www.example.com`          |
| **User input**              | Regular      | None           | None           | *`password`*               |
| **Values**                  | Regular      | None           | None           | `3.14159`                  |
| **Variables**               | Regular      | Camelcase      | None           | **`currentSize`**          |
| **Vocabulary**              | Italic       | None           | None           | *Stacking context*         |
| **XML schema elements**     | Bold         | Lowercase      | None           | **`xml:space`**            |

## Final publishing review

- **Hit the mark.** Review the project brief and make sure the objective and key points are clear.
- **Get a second opinion.** Find someone unrelated to the work to offer feedback.
- **Read your work thoroughly.** Read it forward, and also backward. It may sound silly, but you can spot errors that the human brain negates when reading in a forward scan.
- **Read only the headings.** Then read the first sentence of each paragraph. Check if they are sensible, consistent, and not repetitive structure.
- **Check for keywords in titles and headings.** Titles and headings help readers scan and help search engines find your content. Make sure you include relevant keywords in the first few words.
- **Remove redundant elements.** Do not repeat descriptions that are found later in the document.
- **Pay attention to the spell checker.** Eliminate spelling errors, but spell checkers can not understand context so some warnings or suggestions might be misleading.
- **Take a break.** Leave the finished piece alone for a day. Read it again tomorrow — you may see things you missed.

## Global communication

- Choose colors carefully as some colors might have religious, cultural, or political significance. However, neutral and brand colors are fine.
- Choose images that are appropriate worldwide by avoiding holiday, major landmarks, signs, and other art that is relevant to only a particular group of people.
- Limit graphics and animations on web as some regions have low internet bandwidth.
- Write descriptive alt text for images for accessibility to visually-impaired people and people who are unaware of the context for the image.
- Store art in separate files and link to it within the document. Localizers can modify art that is not embedded within a document.
- Check restrictions on imported content in regions where the content will be used. Be especially careful with maps, which might have an improper treatment of a disputed area, and art that is not owned or in public domain, which might require license agreements.
- Use title-style capitalization for currency names. Prefer *US Dollars* as a currency when neutral depiction of monetary value is concerned.
- When referencing to specific amounts of money, use the currency code followed by the amount with a space.
- Consider how fictitious scenarios may be perceived in other cultures, and avoid mentioning real places, people, and technology or standards that are not used worldwide.
- In forms that collect user name information, provide fields for *First name* and *Last name*. The *Title* and *Middle name* fields should be optional.
- In forms that collect user address information, provide long enough field that can include address appropriate for a variety of locale. Use *State / Province*, *Country / Region*, and *Postal code* fields to accommodate various locale and disputed territories.
- In forms that collect user contact information, provide enough space in *Email* and *Phone number* fields to accommodate long email addresses and phone numbers.
- Use the date format *month date, year* with *month* spelled-out with its name and both *date* and *year* are numerals.
- Use the time format *hour:minute:second (UTC+hh:mm)* with *hour*, *minute*, *second*, *hh*, and *mm* as numerals padded with zeroes.
- Support browsers likely to be used by the relevant audience. Design content so fonts can be substituted if the specified font is not available, and use standard HTML tags instead of proprietary tags.
- Minimize load time by keeping page size small and include text-only versions for larger content. Design pages so text loads first, followed by graphics, so pages are usable before they are finished loading.
- Support multiple languages, and reading from both right-to-left and left-to-right. Allow space for text expansion due to translation and localization.
- Comply with local laws and license restrictions when international delivery in concerned.
- Only link to websites that are accessible and useful worldwide. If a link must be included that is not globally relevant, provide informant notice.
- Write short, simple sentences. Punctuating a sentence with more than a few commas and end punctuation usually indicates a complex sentence. Consider breaking it into multiple sentences or replacing with lists and tables.
- Use active voice and indicative mood for descriptions. Use imperative mood in procedures.
- Avoid idioms, colloquial expressions, culture-specific references, and modifier stacks.
- Keep adjectives and adverbs close to the words they modify, and avoid linking more than three phrases or clauses by using coordinate conjunctions.
- Use one word for a concept and use it consistently. Avoid using synonyms to refer to the same concept or feature, and do not use the same word to refer to multiple concepts or features.

## Grammar

### Verbs

#### Verb tense

In the present tense, the action is happening now. The present tense is often easier to read and understand than the past or future tense. It is the best choice for most content.

| Present Simple                 | Simple Past                 | Simple Future                 |
| ------------------------------ | --------------------------- | ----------------------------- |
| I *read*.                      | I *read*.                   | I *will read*.                |
| **Present Continuous**         | **Past Continuous**         | **Future Continuous**         |
| I *am reading*.                | I *was reading*.            | I *will be reading*.          |
| **Present Perfect**            | **Past Perfect**            | **Future Perfect**            |
| I *have read*.                 | I *had read*.               | I *will have read*.           |
| **Present Perfect Continuous** | **Past Perfect Continuous** | **Future Perfect Continuous** |
| I *have been reading*.         | I *had been reading*.       | I *will have been reading*.   |

#### Moods of verb

The mood of the verb expresses the author's intent. Use the indicative mood most of the time. Do not switch moods within a sentence.

| Mood            | Usage                                                        | Example                                     |
| --------------- | ------------------------------------------------------------ | ------------------------------------------- |
| **Indicative**  | Factual statements, questions, assertions, and explanations. | English is the most widely used language.   |
| **Imperative**  | Instructions, procedures, direct commands, requests.         | Use English language.                       |
| **Subjunctive** | Wishes, hypotheses, and suggestions.                         | We recommend that you use English language. |

#### Active and passive voice

Voice is either active or passive. Use the active voice most of the time.

- In active voice, the subject performs the action.
- In passive voice, the subject is the receiver of the action.

| Voice       | Usage                                                           | Example                               |
| ----------- | --------------------------------------------------------------- | ------------------------------------- |
| **Active**  | Most of the content.                                            | You are not able to find the website. |
| **Passive** | Errors, warnings, or notifications to avoid blaming the reader. | The website can not be found.         |

#### Verb agreements

Verbs have singular and plural forms. Use the verb that agrees with the subject of the sentence in number.

| Subject                                        | Verb                        | Example                                     |
| ---------------------------------------------- | --------------------------- | ------------------------------------------- |
| A group of things                              | Singular                    | A group of things is called a collection.   |
| Two or more singular things connected by *and* | Plural                      | Thing and thing are called two things.      |
| Two or more singular things connected by *or*  | Singular                    | Thing or thing is called a thing.           |
| Singular and plural things connected by *or*   | *Match the closest subject* | Thing or things are called thing or things. |

### Nouns and pronouns



## Unbiased communication

- Use gender-neutral alternatives for common terms and generic references.
- Refer to a person's role instead of identifying them by a pronoun.
- When writing about a real person, use the pronouns that person prefers.
- Represent diverse perspectives and circumstances, and be inclusive of everyone.
- Avoid stereotypes and mentions of politically disputed topics.
- Do not make generalization about a specific group of people or place, even if it is positive or neutral.
- Do not use terms that are slang, profane, derogatory, carry unconscious racial bias, or associated with military action, politics, or historical events.
- Use title-style capitalization for Asian, Black, White, African American, Hispanic, Latin, Native American, Alaska Native, Native Hawaiian, Pacific Islander, and Indigenous Peoples.

