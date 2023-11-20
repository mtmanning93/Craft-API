# Manual Testing

- [/](#endpoint-tests)
- [/profiles/](#profiles-tests)
- [/profiles/<int:pk>/](#profiles-tests)
- [/posts/](#posts-tests)

## `/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Navigate to the 'root' url as a logged out user | GET | Displays welcome message | 200 | Pass | - |
| 2 | Navigate to the 'root' url as a logged in user | GET | Displays welcome message | 200 | Pass | - |

<details>
<summary>Test 1 Screenshots</summary>

![Test 1](README_images/testing/manual/root.png)
</details>
<details>
<summary>Test 2 Screenshots</summary>

![Test 2](README_images/testing/manual/root-login.png)
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
| 28 | Navigate to a post owned by the user, update the title field to a title longer than 100 characters, click 'PUT'. | PUT | Validation error is raised with message: "Ensure this field has no more than 100 characters." | 400 | Pass | - |
| 29 | Navigate to a post owned by the user, update the content field, click 'PUT'. | PUT | Content field updates in the JSON response | 200 | Pass | - |
| 30 | Update the post image file selector, with a file thats not an image. | PUT | Validation error is raised with message: "Upload a valid image. The file you uploaded was either not an image or a corrupted image." | 400 | Pass | - |
| 31 | Update the post image file selector, with an image thats larger than 2mb. | PUT |  Validation error is raised with message: "Image size larger than 2MB!" | 400 | Pass | - |
| 32 | Update the post image file selector, with an image thats wider than 4096px. | PUT | Validation error is raised with message: "Image width larger than 4096px!" | 400 | Pass | - |
| 33 | Update the post image file selector, with an image thats higher than 4096px. | PUT | Validation error is raised with message: "Image height larger than 4096px!" | 400 | Pass | - |
| 34 | Navigate to a post owned by the user, click the delete button. | DELETE | Delete confirmation displays, on confirmation deletes post, post is no longer available in the post list view. | 204 | Pass | - |

| Test Screenshots |              |
|-------------|--------------|
| <details><summary>Test 26</summary> ![Test 26](README_images/testing/manual/posts/post-details.png) </details> | <details><summary>Test 31</summary> ![Test 31](README_images/testing/manual/posts/update-too-large.png) </details> |
| <details><summary>Test 27</summary> ![Test 27](README_images/testing/manual/posts/owner-post-details.png) </details> | <details><summary>Test 32</summary> ![Test 32](README_images/testing/manual/posts/update-too-wide.png) </details> |
| <details><summary>Test 28</summary> ![Test 28](README_images/testing/manual/posts/update-title-invalid.png) </details> | <details><summary>Test 33</summary> ![Test 33](README_images/testing/manual/posts/update-too-high.png) </details> |
| <details><summary>Test 29</summary> ![Test 29](README_images/testing/manual/posts/content-updates.png) </details> | <details><summary>Test 34</summary> ![Test 34 Notification](README_images/testing/manual/posts/delete-notification.png) ![Test 34](README_images/testing/manual/posts/delete-post.png) </details> |
| <details><summary>Test 30</summary> ![Test 30](README_images/testing/manual/posts/update-invalid.png) </details> |  |

----------------------------

| Test Screenshots |              |
|-------------|--------------|
|  |  |
