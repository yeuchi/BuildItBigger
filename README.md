# BuildItBigger 

### Project Overview
In this project, you will create an app with multiple flavors that uses multiple libraries and Google Cloud Endpoints. The finished app will consist of four modules:

1. A Java library that provides jokes
2. A Google Cloud Endpoints (GCE) project that serves those jokes
3. An Android Library containing an activity for displaying jokes
4. An Android app that fetches jokes from the GCE module and passes them to the Android Library for display

![screen shot 2018-05-19 at 1 17 14 pm](https://user-images.githubusercontent.com/1282659/40273595-7a04ceb2-5b88-11e8-9fa4-99f084d60299.png)

### Why this Project?
As Android projects grow in complexity, it becomes necessary to customize the behavior of the Gradle build tool, allowing automation of repetitive tasks. Particularly, factoring functionality into libraries and creating product flavors allow for much bigger projects with minimal added complexity.

### What Will I Learn?
You will learn the role of Gradle in building Android Apps and how to use Gradle to manage apps of increasing complexity. You'll learn to:

- Add free and paid flavors to an app, and set up your build to share code between them
- Factor reusable functionality into a Java library
- Factor reusable Android functionality into an Android library
- Configure a multi-project build to compile your libraries and app
- Use the Gradle App Engine plugin to deploy a backend
- Configure an integration test suite that runs against the local App Engine development server


### How Do I Complete this Project?
#### Step 0: Starting Point
This is the starting point for the final project, which is provided to you in the course repository. It contains an activity with a banner ad and a button that purports to tell a joke, but actually just complains. The banner ad was set up following the instructions here:

https://developers.google.com/mobile-ads-sdk/docs/admob/android/quick-start

You may need to download the Google Repository from the Extras section of the Android SDK Manager.

You will also notice a folder called backend in the starter code. It will be used in step 3 below, and you do not need to worry about it for now.

When you can build an deploy this starter code to an emulator, you're ready to move on.

<img src="https://user-images.githubusercontent.com/1282659/40581472-bc56d12a-611e-11e8-9225-44e7263e1356.png" width="200">

#### Step 1: Create a Java library
Your first task is to create a Java library that provides jokes. Create a new Gradle Java project either using the Android Studio wizard, or by hand. Then introduce a project dependency between your app and the new Java Library. If you need review, check out demo 4.01 from the course code.

Make the button display a toast showing a joke retrieved from your Java joke telling library.

<img src="https://user-images.githubusercontent.com/1282659/40274188-f0f179be-5b95-11e8-9b74-e125a6b82a1e.png" width="200">

#### Step 2: Create an Android Library
Create an Android Library containing an Activity that will display a joke passed to it as an intent extra. Wire up project dependencies so that the button can now pass the joke from the Java Library to the Android Library.

For review on how to create an Android library, check out demo 4.03. For a refresher on intent extras, check out;

http://developer.android.com/guide/components/intents-filters.html

<img src="https://user-images.githubusercontent.com/1282659/40274841-1a5d0604-5ba7-11e8-9bf9-700b2706a5e5.png" width="200">

#### Step 3: Setup GCE
This next task will be pretty tricky. Instead of pulling jokes directly from our Java library, we'll set up a Google Cloud Endpoints development server, and pull our jokes from there. The starter code already includes the GCE module in the folder called backend.

Before going ahead you will need to be able to run a local instance of the GCE server. In order to do that you will have to install the Cloud SDK:

https://cloud.google.com/sdk/docs/

Once installed, you will need to follow the instructions in the Setup Cloud SDK section at:

https://cloud.google.com/endpoints/docs/frameworks/java/migrating-android

Note: You do not need to follow the rest of steps in the migration guide, only the Setup Cloud SDK.

Start or stop your local server by using the gradle tasks as shown in the following screenshot:

![screen shot 2018-05-19 at 5 20 22 pm](https://user-images.githubusercontent.com/1282659/40273622-f7562e60-5b88-11e8-861e-6007da37fc4b.png)

Once your local GCE server is started you should see the following at localhost:8080
This is a bit tricky; thanks to some tips found on the forum.
https://discussions.udacity.com/t/build-it-bigger-error-while-running-appenginedeploy-gce/653651
1. Don’t bother with the error from appEngineDeploy.
2. Sometime it will error onStart, execute Stop first.
3. We don’t need to deploy it on AppEngine.. Just run it local.

![screen shot 2018-05-26 at 2 50 08 pm](https://user-images.githubusercontent.com/1282659/40579751-bcb3ddc2-60f4-11e8-83b1-d3ade3e5e36b.png)

Now you are ready to continue!

Introduce a project dependency between your Java library and your GCE module, and modify the GCE starter code to pull jokes from your Java library. Create an AsyncTask to retrieve jokes using the template included int these instructions. Make the button kick off a task to retrieve a joke, then launch the activity from your Android Library to display it.

(left) is my app retrieving the message from backend example.
(right) backend is retrieving joke from jokeLib.

<img src="https://user-images.githubusercontent.com/1282659/40580318-68d474ac-6101-11e8-8465-ea2230286482.png" width="200"><img src="https://user-images.githubusercontent.com/1282659/40581478-0c76b4d6-611f-11e8-84fa-29f1892fd1d4.png" width="200">

#### Step 4: Add Functional Tests
Add code to test that your Async task successfully retrieves a non-empty string. For a refresher on setting up Android tests, check out demo 4.09.

![test](https://user-images.githubusercontent.com/1282659/40581536-f9ebe960-6120-11e8-9bfc-f0aae299f789.png)

#### Step 5: Add a Paid Flavor

Select the build variant to see (edit) free vs paid files.

![variant](https://user-images.githubusercontent.com/1282659/40588046-5343dbae-619d-11e8-8154-43627c930775.png)

Add free and paid product flavors to your app. Remove the ad (and any dependencies you can) from the paid flavor.

<img src="https://user-images.githubusercontent.com/1282659/40588009-ce61d86e-619c-11e8-9775-654726f84417.png" width="200"><img src="https://user-images.githubusercontent.com/1282659/40588010-d02513c8-619c-11e8-8dd3-0ee2e46b2b8f.png" width="200">


### Optional Tasks
For extra practice to make your project stand out, complete the following tasks.

### Add Interstitial Ad
Follow these instructions to add an interstitial ad to the free version. Display the ad after the user hits the button, but before the joke is shown.

https://developers.google.com/mobile-ads-sdk/docs/admob/android/interstitial

### Add Loading Indicator
Add a loading indicator that is shown while the joke is being retrieved and disappears when the joke is ready. The following tutorial is a good place to start:

http://www.tutorialspoint.com/android/android_loading_spinner.htm

### Configure Test Task
To tie it all together, create a Gradle task that:

Launches the GCE local development server
Runs all tests
Shuts the server down again

### Submission and Evaluation
Your project will be evaluated by a Udacity Code Reviewer according to this rubric . Be sure to review it thoroughly before you submit. All criteria must "meet specifications" in order to pass.

Note: Please make sure you clean your project before creating a zip file or pushing code to a GitHub repository. You can clean your project by following these instructions.

If you are using GitHub to host your projects, please make sure the code you want to submit for review is in the master branch of your repository.

IMPORTANT: If you're submitting via a public Github repository, please make sure any external API key that you utilize, has been removed from your code. It's highly unsafe (and often breaks the Terms of Service) to include API keys in public repos, so you need to remove yours. You can add a note in a README file where a reviewer should go to insert their API key. Reviewers have been trained to expect this situation.

IMPORTANT: Make sure not to forget to move all the hardcoded Strings in your project to the strings.xml file. If you are unsure how to do this, revisit this video in Advanced Android Apps.

If you have any problems submitting your project, please email us at android-project@udacity.com. Due to the high volume of submissions, the turnaround for your project can take up to a week.

Each Android ND project will be reviewed against the Common Project Requirements, in addition to its project-specific rubric.

## Project Rubric
Your project will be evaluated by a Udacity Code Reviewer according to this rubric.

A summary of the rubric is provided below.

### Required Components
- Project contains a Java library for supplying jokes
- Project contains an Android library with an activity that displays jokes passed to it as intent extras.
- Project contains a Google Cloud Endpoints module that supplies jokes from the Java library. Project loads jokes from GCE module via an async task. Note that this GCE module doesn't need to be deployed to a server. Local testing works fine.
- Project contains connected tests to verify that the async task is indeed loading jokes.
- Project contains paid/free flavors. The paid flavor has no ads, and no unnecessary dependencies.

### Required Behavior
App retrieves jokes from Google Cloud Endpoints module and displays them via an Activity from the Android Library.
Optional Components
Once you have a functioning project, consider adding more features to test your Gradle and Android skills. Here are a few suggestions:

Make the free app variant display interstitial ads between the main activity and the joke-displaying activity.
Have the app display a loading indicator while the joke is being fetched from the server.
Write a Gradle task that starts the GCE dev server, runs all the Android tests, and shuts down the dev server.

### References

1. "This is a test to show how to use expresso to check if a toast was displayed" by Bruno de Lima e Silva (brunodles), GithubGist
https://gist.github.com/brunodles/badaa6de2ad3a84138d517795f15efc7
