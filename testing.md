# Testing

## Contents

- [Automated Testing](#automated-testing)
- [Coverage](#coverage)
- [Python Linter](#python-linter)
- [Manual Testing](#manual-testing)
    - [/](#tests)
    - [/profiles/](#profiles-tests)
    - [/profiles/pk/](#profilesintpk-tests)
    - [/posts/](#posts-tests)
    - [/posts/pk/](#postsintpk-tests)
    - [/comments/](#comments-tests)
    - [/comments/pk/](#commentsintpk-tests)
    - [/companies/](#companies-tests)
    - [/companies/pk/](#companiesintpk-tests)
    - [/approvals/](#approvals-tests)
    - [/approvals/pk/](#approvalsintpk-tests)
    - [/likes/](#likes-tests)
    - [/likes/pk/](#likesintpk-tests)
    - [/followers/](#followers-tests)
    - [/followers/pk/](#followersintpk-tests)

[⏪ Main README](README.md)

## Automated Testing

To test test the overall functionality of the craft_api project and its containing apps, automated testing was implemented with the goal of testing all views, serializers, custom permissions and models which were created during the build. During the testing phase there was **92** tests passed, including **197** assertions. There are many more tests which could possibly be written and cover more situations, however, the goal with the current applicaiton scope was to simple cover as much functionality as possible using `coverage` as a testing tool.

Initially when building the testcases I had to learn the difference bewteen TestCase and APITestCase, however after reading the necessary documents it was clear that APITestCase would be useful for testing api endpoints therefore it was used for testiing views, serializers and permissions. TestCase was useful for testing the models as this doesnt rewuire the same functionality in the tests.

The written tests can be found in the `<App>/tests/` files of all apps in the API.

*Some resources I used to build knowledge and write tests can be found in [README.md](README.md) credits section.*

[⏫ contents](#contents)

## Coverage

I used `coverage` throughout the testing phase to measure the percentage of each apps covered code. `Coverage` highlighted which specific lines of code were not tested when running the html server. This enabled me to build more tests to target these lines of code. I seperated each apps tests into seperate files for clarity, each app had the folowing tests file structure:

    - app/
        - tests/
            - __init__.py
            - test_models.py
            - test_serializers.py
            - test_views.py

After using `coverage` I was able to reach **100%** of the code covered within all apps.

The main project file 'craft_api' only reached **90%** coverage. This is due to wsgi.py and asgi.py files which are created by Django as entry points for different application servers and the settings.py file.

To run `coverage` for the entire application, type in command line:

    coverage run manage.py test

To run `coverage` for each app, type in command line:

    coverage run --source=<app_name> manage.py test <app_name>

<details>
<summary>Coverage Reports Screenshots</summary>

![Approvals report](README_images/testing/approvals_cov.png)
![Comments report](README_images/testing/comments_cov.png)
![Companies report](README_images/testing/companies_cov.png)
![Craft_api 90% report](README_images/testing/craft_api_cov.png)
![Followers report](README_images/testing/followers_cov.png)
![Likes report](README_images/testing/likes_cov.png)
![Posts report](README_images/testing/posts_cov.png)
![Profiles report](README_images/testing/profiles_cov.png)
</details>
<br>

[⏫ contents](#contents)

## Python Linter

To check for syntax errors in the project's Python code I used `pycodestyle` *(formerly pep8)*. Using this I was able to test my code from inside the command line. Its a fast and easy way to heck the syntax as it returns the file name and lines of the error.

To install `pycodestyle` in the command line:

    pip install pycodestyle

Then to test the files in the command line:

    pycodestyle <file_name>
    or
    pycodestyle .

When initially running the linter there were a few errors which I addressed and corrected. After these corrections the only errors left were *'E501 line too long'*. These were mostly found in the migration files automatically created during the `makemigration` command. After updating these there were no more errors within my files.

To check I ran the following in the command line:

    pycodestyle <app_name> *(all apps)*
    pycodestyle . (only errors shown in .vscode files)

[⏫ contents](#contents)

## Manual Testing

To accompany the automated testing, the Craft-API underwent manual testing on all custom endpoints, covering all CRUD functionality, serialised data, and checking `to_representation` methods. Below are the tests carried out at each API endpoint, they have been seperated by custom endpoint and details the HTTP method used for the test, and expected outcomes. If the test failed the action which was taken to ensure a Pass was made.

All tests include screenshots, in order for larger viewing they are seperate to the tests. To view the screenshot select the test number in the screenshots table below the main tests table for each endpoint.

## `/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Navigate to the 'root' url as a logged out user | GET | Displays welcome message | 200 | Pass | - |
| 2 | Navigate to the 'root' url as a logged in user | GET | Displays welcome message | 200 | Pass | - |

| Test Screenshots |
|-------------|
| <details><summary>Test 1</summary> ![Test 1](README_images/testing/manual/root/root.png) </details> |
| <details><summary>Test 2</summary> ![Test 2](README_images/testing/manual/root/root-login.png) </details> |

[⏫ contents](#contents)

## `/profiles/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | Navigate to the the profiles page url as a logged out user | GET | Returns a lists of all site profiles. | 200 | Pass | - |
| 4 | Navigate to the the profiles page url as a logged in user | GET | Returns a lists of all site profiles. | 200 | Pass | - |  |

| Test Screenshots |
|-------------|
| <details><summary>Test 3</summary> ![Test 3](README_images/testing/manual/profiles/profiles.png) </details> |
| <details><summary>Test 4</summary> ![Test 4](README_images/testing/manual/profiles/profiles-login.png) </details> |

[⏫ contents](#contents)

## `/profiles/<int:pk>/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | Navigate to a profile details page using `/profiles/1/` url as a logged out user | GET | Displays profile details of the profile with id: 1 | 200 | Pass | - |
| 6 | Navigate to a profile details page using `/profiles/1/` url as a logged in user | GET | Displays profile details of the profile with id: 1, if owner html update from displays. | 200 | Pass | - |
| 7 | Login and navigate to `/profiles/1/` (owned profile) update the HTML form name field and click 'PUT' | PUT | The profiles JSON name field is updated with the updated name | 200 | Pass | - |
| 8 | Login and navigate to `/profiles/1/` (owned profile) update the HTML form name field with 'Christopher Alexander Harrington III Esquire Jr.' (more than 75 characters) and click 'PUT' | PUT | Validation error is raised with message 'Ensure this field has no more than 75 characters.' | 400 | Pass | - |
| 9 | Login and navigate to `/profiles/1/` (owned profile) update the HTML form bio field and click 'PUT' | PUT | The profiles JSON bio field is updated with the updated information | 200 | Pass | - |
| 10 | Login and navigate to `/profiles/1/` (owned profile) update the HTML form bio field with more than 200 characters and click 'PUT' | PUT | Validation error is raised with message 'Ensure this field has no more than 200 characters.' | 400 | Pass | - |
| 11 | Login and navigate to `/profiles/1/` (owned profile) update the HTML form job field and click 'PUT' | PUT | The profiles JSON job field is updated with the updated information | 200 | Pass | - |
| 12 | Login and navigate to `/profiles/1/` (owned profile) update the HTML form job field with more than 75 characters and click 'PUT' | PUT | Validation error is raised with message 'Ensure this field has no more than 75 characters.' | 400 | Pass | - |
| 13 | Login and navigate to `/profiles/1/` (owned profile) update the image file field with a valid new image and click 'PUT' | PUT | The profiles JSON image field is updated with the updated information | 200 | Pass | - |
| 14 | Login and navigate to `/profiles/1/` (owned profile) update the image file field with a file which is not an image file type and click 'PUT' | PUT | Validation error is raised with message 'Upload a valid image. The file you uploaded was either not an image or a corrupted image.' | 400 | Pass | - |
| 15 | Login and navigate to `/profiles/1/` (owned profile) update the HTML form employer field by selecting an option form the dropdown and click 'PUT' | PUT | The profiles JSON employer field is updated with the updated employer information | 200 | Pass | - |
| 16 | Login and navigate to `/profiles/1/` (owned profile) update the HTML form employer field with the '-----' (none) option and click 'PUT' | PUT | The employer field is reset to null. | 200 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 5</summary> ![Test 5](README_images/testing/manual/profiles/profile-details.png) </details> | <details><summary>Test 13</summary> ![Test 13](README_images/testing/manual/profiles/image-valid.png) </details> |
| <details><summary>Test 6</summary> ![Test 6](README_images/testing/manual/profiles/profile-details-login.png) </details> | <details><summary>Test 14</summary> ![Test 14](README_images/testing/manual/profiles/not-image.png) </details> |
| <details><summary>Test 7</summary> ![Test 7 Before Update](README_images/testing/manual/profiles/profile-form.png) ![Test 7 After Update](README_images/testing/manual/profiles/update-profile-name.png) </details> | <details><summary>Test 15</summary> ![Test 15](README_images/testing/manual/profiles/employer-update.png) </details> |
| <details><summary>Test 8</summary> ![Test 8](README_images/testing/manual/profiles/profiles-name-error.png) </details> | <details><summary>Test 16</summary> ![Test 16](README_images/testing/manual/profiles/employer-null.png) </details> |

[⏫ contents](#contents)

## `/posts/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 17 | Navigate to the /posts/ url as a logged out user | GET | Returns a lists of all site posts, including a count and pagination url links. | 200 | Pass | - |
| 18 | Navigate to the /posts/ url as a logged in user | GET | Returns a lists of all site posts, including a count and pagination url links, plus a logged in user will see a update html form. | 200 | Pass | - |
| 19 | Navigate to the /posts/ url as a logged in user fill out the html form to create a valid post, click 'Post' | POST | Directs user to the new created post details page, new post can be seen in the post list. | 201 | Pass | - |
| 20 | Navigate to the /posts/ url as a logged in user fill out the html form title field with a title longer than 100 characters, click 'Post' | POST | Validation error is raised with message: 'Ensure this field has no more than 100 characters.' | 400 | Pass | - |
| 21 | Navigate to the /posts/ url as a logged in user fill out the html form, add a file which is not an image to the image field, click 'Post' | POST | Validation error is raised with message: "Upload a valid image. The file you uploaded was either not an image or a corrupted image." | 400 | Pass | - |
| 22 | Navigate to the /posts/ url as a logged in user fill out the html form, add an image which is over 2mb in size, click 'Post' | POST | Validation error is raised with message: "Image size larger than 2MB!" | 400 | Pass | - |
| 23 | Navigate to the /posts/ url as a logged in user fill out the html form, add an image which is over 4096px in width, click 'Post' | POST | Validation error is raised with message: "Image width larger than 4096px!" | 400 | Pass | - |
| 24 | Navigate to the /posts/ url as a logged in user fill out the html form, add an image which is over 4096px in height, click 'Post' | POST | Validation error is raised with message: "Image height larger than 4096px!" | 400 | Pass | - |
| 25 | Navigate to the /posts/ url as a logged in user fill out the html form with valid data, do not add an image, click 'Post' | POST | Post instance is created and the image field is populated with the default site. | 400 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 17</summary> ![Test 17](README_images/testing/manual/posts/posts-list.png) </details> | <details><summary>Test 22</summary> ![Test 22](README_images/testing/manual/posts/image-too-big.png) </details> |
| <details><summary>Test 18</summary> ![Test 18](README_images/testing/manual/posts/posts-lists-login.png) </details> | <details><summary>Test 23</summary> ![Test 23](README_images/testing/manual/posts/image-too-wide.png) </details> |
| <details><summary>Test 19</summary> ![Test 19](README_images/testing/manual/posts/create-post-form.png) ![Test 19](README_images/testing/manual/posts/created-post.png) ![Test 19](README_images/testing/manual/posts/new-post-list.png) </details> | <details><summary>Test 24</summary> ![Test 24](README_images/testing/manual/posts/image-too-high.png) </details> |
| <details><summary>Test 20</summary> ![Test 20](README_images/testing/manual/posts/invalid-title.png) </details> | <details><summary>Test 25</summary> ![Test 25](README_images/testing/manual/posts/default-post-image.png)</details> |
| <details><summary>Test 21</summary> ![Test 21](README_images/testing/manual/posts/posts-lists-login.png) </details> |  |

[⏫ contents](#contents)

## `/posts/<int:pk>/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | Navigate to a post details page url as a logged out user | GET | Returns a lists of all related post details. | 200 | Pass | - |
| 27 | Navigate to the the post page url of a post owned by user | GET | Returns a lists of all post details, including Delete button and html form beneath. | 200 | Pass | - |  |
| 28 | Navigate to the the post page url of a post owned by user | GET | Returns a lists of all post details, including the is_owner field which is set to 'true'. | 200 | Pass | - |
| 29 | Navigate to a post owned by the user, update the title field to a title longer than 100 characters, click 'PUT'. | PUT | Validation error is raised with message: "Ensure this field has no more than 100 characters." | 400 | Pass | - |
| 30 | Navigate to a post owned by the user, update the content field, click 'PUT'. | PUT | Content field updates in the JSON response | 200 | Pass | - |
| 31 | Update the post image file selector, with a file thats not an image. | PUT | Validation error is raised with message: "Upload a valid image. The file you uploaded was either not an image or a corrupted image." | 400 | Pass | - |
| 32 | Update the post image file selector, with an image thats larger than 2mb. | PUT |  Validation error is raised with message: "Image size larger than 2MB!" | 400 | Pass | - |
| 33 | Update the post image file selector, with an image thats wider than 4096px. | PUT | Validation error is raised with message: "Image width larger than 4096px!" | 400 | Pass | - |
| 34 | Update the post image file selector, with an image thats higher than 4096px. | PUT | Validation error is raised with message: "Image height larger than 4096px!" | 400 | Pass | - |
| 35 | Navigate to a post owned by the user, click the delete button. | DELETE | Delete confirmation displays, on confirmation deletes post, post is no longer available in the post list view. | 204 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 26</summary> ![Test 26](README_images/testing/manual/posts/post-details.png) </details> | <details><summary>Test 31</summary> ![Test 31](README_images/testing/manual/posts/update-invalid.png) </details> |
| <details><summary>Test 27</summary> ![Test 27](README_images/testing/manual/posts/owner-post-details.png) </details> | <details><summary>Test 32</summary> ![Test 32](README_images/testing/manual/posts/update-too-large.png) </details> |
| <details><summary>Test 28</summary> ![Test 28](README_images/testing/manual/posts/is-owner.png) </details> | <details><summary>Test 33</summary> ![Test 33](README_images/testing/manual/posts/update-too-wide.png) </details> |
| <details><summary>Test 29</summary> ![Test 29](README_images/testing/manual/posts/update-title-invalid.png) </details> | <details><summary>Test 34</summary> ![Test 34](README_images/testing/manual/posts/update-too-high.png) </details> |
| <details><summary>Test 30</summary> ![Test 30](README_images/testing/manual/posts/content-updates.png) </details> | <details><summary>Test 35</summary> ![Test 35 Notification](README_images/testing/manual/posts/delete-notification.png) ![Test 35](README_images/testing/manual/posts/delete-post.png) </details> |

[⏫ contents](#contents)

## `/comments/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 36 | Navigate to the '/comments/' url as a logged out user | GET | Returns a lists of all site comments, including count field and pagination urls. | 200 | Pass | - |
| 37 | Log in and navigate to the '/comments/' url | GET | Returns a lists of all site profiles, including a create comment HTML form. | 200 | Pass | - |  |
| 38 | Log in and navigate to the '/comments/' url, locate the is_owner field. | GET | The logged in user should see the is_owner field populated with 'true' if they own the comment | 200 | Pass | - |  |
| 39 | In the create comment HTML form create a comment by selecting a post from the dropdown and write a message in the content field. | POST | Creates a comment instance, redirects the user to the related comment details page, the comment details match the input details. Comment can also be found in the comments list. | 201 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 36</summary> ![Test 36](README_images/testing/manual/comments/comments-list.png) </details> | <details><summary>Test 38</summary> ![Test 38](README_images/testing/manual/comments/is-owner-true.png) </details> |
| <details><summary>Test 37</summary> ![Test 37](README_images/testing/manual/comments/comments-login.png) </details> | <details><summary>Test 39</summary> ![Test 39](README_images/testing/manual/comments/comment-details.png) ![Test 39 List](README_images/testing/manual/comments/comments-new-list.png) </details> |

[⏫ contents](#contents)

## `/comments/<int:pk>/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 40 | As a logged out user navigate to '/comments/1/', locate the 'is_owner' field. | GET | The is_owner field is set to false. | 200 | Pass | - |
| 41 | As  logged in user navigate to a comments details page of a comment you own. | GET | The is_owner field is set to true within the JSON response, Delete button is visible, and the update HTML form is visible below. | 200 | Pass | - |
| 42 | Navigate to the HTML form and update the content field, click 'PUT' | PUT | Comment instance is created, the updated comment details are visible in the comment details view. | 200 | Pass | - |
| 43 | Locate the 'created_on' field. | GET | The created on field is displayed in a human 'natural' format. For example, "1 month, 1 week ago" | N/A | Pass | - |
| 44 | Locate the 'updated_on' field. | GET | The updated on field is displayed in a human 'natural' format. For example, "1 month, 1 week ago" | N/A | Pass | - |
| 45 | Update a comment instance, locate the updated on field after valid submission | PUT | The updated on field is displayed as "now". | 200 | Pass | - |
| 46 | Attempt to update the comment form with no input | PUT | Validation error is raised with message: "This field may not be blank." | 400 | Pass | - |
| 47 | Delete a comment instance owned by the user | DELETE | The deletion confirmation is displayed, if confirmed the instance is removed. | 204 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 40</summary> ![Test 40](README_images/testing/manual/comments/is-owner-false.png) </details> | <details><summary>Test 44</summary> ![Test 44](README_images/testing/manual/comments/updated-on.png) </details>  |
| <details><summary>Test 41</summary> ![Test 41](README_images/testing/manual/comments/owner-comment-details.png) </details> | <details><summary>Test 45</summary> ![Test 45](README_images/testing/manual/comments/now.png) </details> |
| <details><summary>Test 42</summary> ![Test 42 Before](README_images/testing/manual/comments/update-before.png) ![Test 42 After](README_images/testing/manual/comments/update-after.png) </details> | <details><summary>Test 46</summary> ![Test 46](README_images/testing/manual/comments/no-input.png) </details> |
| <details><summary>Test 43</summary> ![Test 43](README_images/testing/manual/comments/created-on.png) </details> | <details><summary>Test 47</summary> ![Test 47 Modal](README_images/testing/manual/comments/delete-comment-confirm.png) ![Test 47](README_images/testing/manual/comments/delete-comment.png) </details> |

[⏫ contents](#contents)

## `/companies/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 48 | Navigate to the '/companies/' url as a logged out user | GET | Returns a list of all company instances from the site, including a count field and the pagination url extensions. | 200 | Pass | - |
| 49 | Navigate to the '/companies/' url as a logged in user | GET | Returns a list of all company instances from the site, including a count field and the pagination url extensions, the create company HTML form is available below. | 200 | Pass | - |
| 50 | Submit the create company form with no data | POST | Validation error is raised. | 400 | Pass | - |
| 51 | Submit the create company form with no data in the 'name' field | POST | Validation error is raised with message: "This field may not be blank.". | 400 | Pass | - |
| 52 | Submit the create company form with only name data | POST | Company instance is created. | 201 | Pass | - |
| 53 | Create a company with duplicate name and location fields as an already created company. | POST | Validation error raised with message: "A company with that title and location already exists." | 400 | Pass | - |
| 54 | Create a company with the name field longer that 100 characters. | POST | Validation error raised name too long. | 400 | Pass | - |
| 55 | Create a company with the location field longer that 100 characters. | POST | Validation error raised location too long. | 400 | Pass | - |
| 56 | Create a company with the type field longer that 100 characters. | POST | Validation error raised type too long. | 400 | Pass | - |
| 57 | Create a new company by filling out the html form with valid data | POST | Company is created, redirecting user to the company details, all relevant details are present, the company can be found in the companies list. | 201 | Pass | - |
| 58 | As a new user attempt to create a 4th company. | POST | Validation error is raised, users can only create a maximum of three companies per profile. The message is "You have reached the max profile limit of 3 companies." | 400 | Pass | - |
| 59 | Create a new company and then navigate to owned profile details, locate the employer dropdown. | GET | The newly created company should be displayed in the employer dropdown list. | 200 | Pass | - |
| 60 | Navigate to a company instance owned by the user and delete. | DELETE | Deletion confirmation modal is displayed, if confirmed the company instance is deleted. | 204 | Pass | - |


| Test Screenshots |                  |                  |
|------------------|------------------|------------------|
| <details><summary>Test 48</summary> ![Test 48](README_images/testing/manual/companies/companies.png) </details> | <details><summary>Test 53</summary> ![Test 53](README_images/testing/manual/companies/duplicate.png) ![Test 53](README_images/testing/manual/companies/duplicate-error.png) </details> | <details><summary>Test 57</summary> ![Test 57](README_images/testing/manual/companies/create-company-form.png) ![Test 57](README_images/testing/manual/companies/created-company.png) </details> |
| <details><summary>Test 49</summary> ![Test 49](README_images/testing/manual/companies/companies-login.png) </details> | <details><summary>Test 54</summary> ![Test 54](README_images/testing/manual/companies/company-name-too-long.png) </details> | <details><summary>Test 58</summary> ![Test 58](README_images/testing/manual/companies/max-three-companies.png) </details> |
| <details><summary>Test 50</summary> ![Test 50](README_images/testing/manual/companies/blank-create-form.png) </details>| <details><summary>Test 55</summary> ![Test 55](README_images/testing/manual/companies/company-location-too-long.png) </details> | <details><summary>Test 59</summary> ![Test 59](README_images/testing/manual/companies/employer-dropdown.png) </details> |
| <details><summary>Test 51</summary> ![Test 51](README_images/testing/manual/companies/blank-name.png) </details> | <details><summary>Test 56</summary> ![Test 56](README_images/testing/manual/companies/company-type-too-long.png) </details> | <details><summary>Test 60</summary> ![Test 60](README_images/testing/manual/companies/delete-company-modal.png) ![Test 60 Deleted](README_images/testing/manual/companies/company-deleted.png) </details> |
| <details><summary>Test 52</summary> ![Test 52](README_images/testing/manual/companies/only-name.png) </details> |  |  |

[⏫ contents](#contents)

## `/companies/<int:pk>/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 61 | Navigate to a company details page for example '/companies/12/' | GET | Displays the relevant company details, the company id field matches the url input. | 200 | Pass | - |
| 62 | Login and navigate to company details page of a company owned by the user. | GET | Displays the relevant company details, the company id field matches the url input, additionally the is_owner field is set to 'true', Delete button and HTML update form visible. | 200 | Pass | - |
| 63 | Update the company details with the name field longer that 100 characters, click 'PUT'. | PUT | Validation error raised name too long. | 400 | Pass | - |
| 64 | Update the company details with the location field longer that 100 characters, click 'PUT'. | PUT | Validation error raised location too long. | 400 | Pass | - |
| 65 | Update the company details with the type field longer that 100 characters, click 'PUT'. | PUT | Validation error raised type too long. | 400 | Pass | - |
| 66 | Update the company with duplicate name and location fields as an already created company. | POST | Validation error raised with message: "A company with that title and location already exists." | 400 | Fail | Pass - In order to check for duplicate instances on PUT request, the update generic view was overriden with a perform_update method. The logic was copied from the perform_create and validation methods used in the create generic view in `companies/views.py`. With this update the company is correctly validated on PUT request. |
| 67 | Update profiles employer field with the a company instance, then navigate to this companies details url. | PUT/GET | Companies employee_count field has increased by 1 | 200 | Pass | - |
| 68 | Update profiles employer field with the no company instance '--------', then navigate to this companies details url. | PUT/GET | Companies employee_count field has decreased by 1 | 200 | Pass | - |
| 69 | Set profile employer field to company instance, then delete this company instance | DELETE | The profiles employer instance should be automatically set to 'null' after the company is deleted. | 204 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 61</summary> ![Test 61](README_images/testing/manual/companies/logged-out-details.png) </details> | <details><summary>Test 66</summary> ![Test 66 Fail](README_images/testing/manual/companies/update-duplicate-fail.png) ![Test 66 Pass](README_images/testing/manual/companies/update-duplicate-pass.png) </details> |
| <details><summary>Test 62</summary> ![Test 62](README_images/testing/manual/companies/details-owner.png) </details> | <details><summary>Test 67</summary> ![Test 67](README_images/testing/manual/companies/update-employer.png) ![Test 67 Employee Count](README_images/testing/manual/companies/employee-count.png) </details> |
| <details><summary>Test 63</summary> ![Test 63](README_images/testing/manual/companies/update-name-too-long.png) </details> | <details><summary>Test 68</summary> ![Test 68](README_images/testing/manual/companies/update-employer.png) ![Test 68 Employee Count](README_images/testing/manual/companies/employee-decrease.png) </details> |
| <details><summary>Test 64</summary> ![Test 64](README_images/testing/manual/companies/update-location-too-long.png) </details> | <details><summary>Test 69</summary> ![Test 69 Before Delete](README_images/testing/manual/companies/employer-before-delete.png) ![Test 69 After Delete](README_images/testing/manual/companies/employer-after-delete.png) </details> |
| <details><summary>Test 65</summary> ![Test 65](README_images/testing/manual/companies/update-type-too-long.png) </details> |  |

[⏫ contents](#contents)

## `/approvals/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 70 | Navigate to the 'approvals' url as a logged out user | GET | Displays list of approvals, including count and pagination fields. | 200 | Pass | - |
| 71 | Navigate to the 'approvals' url as a logged in user | GET | Displays list of approvals, including create approval HTML form. | 200 | Pass | - |
| 72 | Check an approvals 'created_on' field is in natural readable format. | GET | Created on field is set to a readable format for example, "1 month, 1 week ago" | N/A | Pass | - |
| 73 | Create an approval by selecting logged in users name in the dropdown menu, click 'POST'. | POST | Validation error is raised with message: "Cannot approve your own profile". | 400 | Pass | - |
| 74 | Create an approval by selected a profile username (not logged in user) in the dropdown menu, click 'POST'. | POST | Approval instance is created. | 201 | Pass | - |
| 75 | Attempt to create an approval with invalid JSON data { "profile": "Test99" }, click 'POST'. | POST | Validation error is raised. | 400 | Pass | - |
| 76 | Attempt to create an approval with duplicate JSON data { "profile": 2 }, click 'POST'. | POST | Validation error is raised. | 400 | Pass | - |
| 77 | Attempt to create an approval with valid JSON data { "profile": <profile.id> }, click 'POST'. | POST | The approval is created. | 201 | Pass | - |
| 78 | After creating an approval check the approved profiles 'approval_count' has incremented by 1. | POST | . | 201 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 70</summary> ![Test 70](README_images/testing/manual/approvals/approvals.png) </details> | <details><summary>Test 75</summary> ![Test 75](README_images/testing/manual/approvals/approvals-invalid-json.png) </details> |
| <details><summary>Test 71</summary> ![Test 71](README_images/testing/manual/approvals/approvals-login.png) </details> | <details><summary>Test 76</summary> ![Test 76](README_images/testing/manual/approvals/json-duplicate.png) </details> |
| <details><summary>Test 72</summary> ![Test 72](README_images/testing/manual/approvals/created-on.png) </details> | <details><summary>Test 77</summary> ![Test 77](README_images/testing/manual/approvals/create-json.png) </details> |
| <details><summary>Test 73</summary> ![Test 73](README_images/testing/manual/approvals/approve-own-profile.png) </details> | <details><summary>Test 78</summary> ![Test 78](README_images/testing/manual/approvals/approval-count.png) </details> |
| <details><summary>Test 74</summary> ![Test 74](README_images/testing/manual/approvals/created.png) </details> |  |

[⏫ contents](#contents)

## `/approvals/<int:pk>/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 79 | Navigate to an approval details owned by user, delete the approval instance. | DELETE | Approval instance is deleted. | 204 | Pass | - |
| 80 | After deleting an approval check the previously approved profiles 'approval_count' has decremented by 1. | DELETE | The profiles 'approval_count field has decremented by 1. | 204 | Pass | - |
| 81 | Navigate to an approval details, locate the 'owner' and 'profile' fields. | GET | The fields are reprsented by the profiles username and not the pk/ id. | N/A | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 79</summary> ![Test 79](README_images/testing/manual/approvals/delete-approval.png) </details> |  |
| <details><summary>Test 80</summary> ![Test 80](README_images/testing/manual/approvals/approval-count-decrement.png) </details> |  |
| <details><summary>Test 81</summary> ![Test 81](README_images/testing/manual/approvals/approval-details.png) </details> |  |

[⏫ contents](#contents)

## `/likes/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 82 | Navigate to the 'likes' url as a logged out user | GET | Displays list of likes, including count and pagination fields. | 200 | Pass | - |
| 83 | Navigate to the 'likes' url as a logged in user | GET | Displays list of likes, including create like HTML form. | 200 | Pass | - |
| 84 | Create a like by selecting a post title in the dropdown menu, click 'POST'. | POST | Like instance is created | 201 | Pass | - |
| 85 | Create a like by selected a post you have already liked from the dropdown menu, click 'POST'. | POST | Validation error is raised: "Possible Duplicate". | 400 | Pass | - |
| 86 | Attempt to create a like with invalid JSON data { "post": "Invalid" }, click 'POST'. | POST | Validation error is raised. | 400 | Pass | - |
| 87 | Attempt to create a like with valid JSON data { "post": <post.id> }, click 'POST'. | POST | The like is created. | 201 | Pass | - |
| 88 | After creating a like check the liked posts 'like_count' has incremented by 1. | POST | likes_count of the related post has increased by 1. | 201 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 82</summary> ![Test 82](README_images/testing/manual/likes/like-list.png) </details> | <details><summary>Test 86</summary> ![Test 86](README_images/testing/manual/likes/invalid-json.png) </details> |
| <details><summary>Test 83</summary> ![Test 83](README_images/testing/manual/likes/like-list-form.png) </details> | <details><summary>Test 87</summary> ![Test 87](README_images/testing/manual/likes/create-json.png) </details> |
| <details><summary>Test 84</summary> ![Test 84](README_images/testing/manual/likes/create-like.png) </details> | <details><summary>Test 88</summary> ![Test 88](README_images/testing/manual/likes/likes-count.png) </details> |
| <details><summary>Test 85</summary> ![Test 85](README_images/testing/manual/likes/duplicate.png) </details> |  |

[⏫ contents](#contents)

## `/likes/<int:pk>/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 89 | Navigate to a like details url owned by the user, delete the instance | DELETE | Like instance is deleted | 204 | Pass | - |
| 90 | After deleting a like check the previously liked posts 'like_count' has decreased by 1. | DELETE | likes_count of the related post has decreased by 1. | 204 | Pass | - |

| Test Screenshots |
|-------------|
| <details><summary>Test 89</summary> ![Test 89](README_images/testing/manual/likes/likes-delete.png) </details> |
| <details><summary>Test 90</summary> ![Test 90](README_images/testing/manual/likes/likes-count-decrement.png) </details> |

[⏫ contents](#contents)

## `/followers/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 91 | Navigate to the '/followers/' url as a logged out user | GET | Displays list of all follower instances, including count and pagination fields. | 200 | Pass | - |
| 92 | Navigate to the '/followers/' url as a logged in user | GET | Displays list of likes, including create follower HTML form. | 200 | Pass | - |
| 93 | Create a follower instance by selecting a profile username from the dropdown menu, click 'POST'. | POST | Follower instance is created | 201 | Pass | - |
| 94 | Create a follower by selecting the logged in users username, click 'POST'. | POST | Validation error is raised: "Possible Duplicate". | 400 | Fail - Follower instance created, users should not be able to follow themselves. | Pass - create a 'perform_create' validation method which checks and raises a validation error if the request.user is equal to the 'followed' fields data (`followers/views.py`) |
| 95 | Create a follower instance using the a profile already 'followed', click 'POST'. | POST | Validation error is raised: "Possible duplicate." | 400 | Pass | - |
| 96 | Attempt to create an approval with valid JSON data { "followed": <profile.id> }, click 'POST'. | POST | The like is created. | 201 | Pass | - |
| 97 | After creating a follower check the followed profiles 'follower_count' has incremented by 1. | POST | follower_count of the related profile has increased by 1. | 201 | Pass | - |
| 98 | After creating a follower check the users profile 'following_count' has incremented by 1. | POST | following_count of the users profile has increased by 1. | 201 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 91</summary> ![Test 91](README_images/testing/manual/followers/follower-list.png) </details> | <details><summary>Test 95</summary> ![Test 95](README_images/testing/manual/followers/duplicate.png) </details> |
| <details><summary>Test 92</summary> ![Test 92](README_images/testing/manual/followers/follower-list-form.png) </details> | <details><summary>Test 96</summary> ![Test 96](README_images/testing/manual/followers/create-json.png) </details> |
| <details><summary>Test 93</summary> ![Test 93](README_images/testing/manual/followers/created.png) </details> | <details><summary>Test 97</summary> ![Test 97 Before Follow](README_images/testing/manual/followers/followers-following-count-zero.png) ![Test 97 After Follow](README_images/testing/manual/followers/follower-count-increase.png) </details> |
| <details><summary>Test 94</summary> ![Test 94 Before](README_images/testing/manual/followers/follow-own-profile-before.png) ![Test 94 After](README_images/testing/manual/followers/follow-own-profile-after.png) </details> | <details><summary>Test 98</summary> ![Test 98 Before Follow](README_images/testing/manual/followers/following-count-before.png) ![Test 98 After Follow](README_images/testing/manual/followers/following-count-after.png) </details> |

[⏫ contents](#contents)

## `/followers/<int:pk>/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 99 | Navigate to a follower details url or a follower instance owned by the user, delete follower instance. | DELETE | Follower instance is destroyed. | 204 | Pass | - |
| 100 | After deleting a follower instance, check the users profile 'following_count' has decreased by 1. | DELETE | following_count of the users profile has decreased by 1. | 204 | Pass | - |
| 101 | After deleting a follower instance check the previously followed profiles 'follower_count' has decreased by 1. | DELETE | follower_count of the related profile has decreased by 1. | 204 | Pass | - |

| Test Screenshots |
|-------------|
| <details><summary>Test 99</summary> ![Test 99](README_images/testing/manual/followers/delete.png) </details> |
| <details><summary>Test 100</summary> ![Test 100 Before Delete](README_images/testing/manual/followers/following-count-after.png) ![Test 100 After Delete](README_images/testing/manual/followers/following-count-before.png) </details> |
| <details><summary>Test 101</summary> ![Test 101 Before Delete](README_images/testing/manual/followers/follower-count-increase.png) ![Test 101 After Delete](README_images/testing/manual/followers/followers-following-count-zero.png) </details> |

[⏫ contents](#contents)

[⏪ Main README](README.md)