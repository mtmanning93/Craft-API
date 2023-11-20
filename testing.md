# Manual Testing

- [/](#tests)
- [/profiles/](#profiles-tests)
- [/profiles/<int:pk>](#profilesintpk-tests)
- [/posts/](#posts-tests)
- [/posts/<int:pk>](#postsintpk-tests)
- [/comments/](#comments-tests)
- [/comments/<int:pk>](#commentsintpk-tests)
- [/companies/](#)
- [/companies/<int:pk>](#companiesintpk-tests)


## `/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Navigate to the 'root' url as a logged out user | GET | Displays welcome message | 200 | Pass | - |
| 2 | Navigate to the 'root' url as a logged in user | GET | Displays welcome message | 200 | Pass | - |

<details>
<summary>Test 1 Screenshots</summary>

![Test 1](README_images/testing/manual/root/root.png)
</details>
<details>
<summary>Test 2 Screenshots</summary>

![Test 2](README_images/testing/manual/root/root-login.png)
</details>

## `/profiles/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | Navigate to the the profiles page url as a logged out user | GET | Returns a lists of all site profiles. | 200 | Pass | - |
| 4 | Navigate to the the profiles page url as a logged in user | GET | Returns a lists of all site profiles. | 200 | Pass | - |  |

<details>
<summary>Test 3 Screenshots</summary> 

![Test 3](README_images/testing/manual/profiles/profiles.png)
</details>
<details>
<summary>Test 4 Screenshots</summary>

![Test 4](README_images/testing/manual/profiles/profiles-login.png)
</details>

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