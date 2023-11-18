# Manual Testing

- [/](#endpoint-tests)
- [/profiles/](#profiles-tests)
- [/profiles/<int:pk>/](#profiles-tests)

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
| 3 | Navigate to the the page url as a logged out user | GET | Returns a lists of all site profiles. | 200 | Pass | - |
| 4 | Navigate to the the page url as a logged in user | GET | Returns a lists of all site profiles. | 200 | Pass | - |

<details>
<summary>Test 3 Screenshots</summary>

![Test 3](README_images/testing/manual/profiles.png)
</details>
<details>
<summary>Test 4 Screenshots</summary>

![Test 4](README_images/testing/manual/profiles-login.png)
</details>

## `/profiles/<int:pk>/` Tests

| **#** | **Test** | **Test HTTP Method** | **Expected Outcome** | **Expected Status Code** | **Result** | **Action Taken To Pass _(if fail)_** |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | Navigate to a profile details page using `/profiles/1/` url as a logged out user | GET | Displays profile details of the profile with id: 1 | 200 | Pass | - |
| 6 | Navigate to a profile details page using `/profiles/1/` url as a logged in user | GET | Displays profile details of the profile with id: 1 | 200 | Pass | - |
| 7 | Login and navigate to `/profiles/<your profile id>/` update the HTML form name field and click 'PUT' | GET | Profiles JSON name field is updated with the updated name | 200 | Pass | - |

<details>
<summary>Test 5 Screenshots</summary>

![Test 5](README_images/testing/manual/root.png)
</details>
<details>
<summary>Test 6 Screenshots</summary>

![Test 6](README_images/testing/manual/root.png)
</details>
<details>
<summary>Test 7 Screenshots</summary>

![Test 7 Before Update](README_images/testing/manual/profile-form.png)
![Test 7 After Update](README_images/testing/manual/update-profile-name.png)
</details>