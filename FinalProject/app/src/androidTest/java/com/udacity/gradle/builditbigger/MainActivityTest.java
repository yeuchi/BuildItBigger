package com.udacity.gradle.builditbigger;

/**
 * Created by ctyeung on 5/26/18.
 */

import android.app.Activity;
import android.support.test.runner.AndroidJUnit4;
import org.junit.Test;
import org.junit.runner.RunWith;
import static junit.framework.Assert.assertEquals;

import android.support.test.rule.ActivityTestRule;
import org.junit.Rule;

import android.content.Context;
import android.support.test.InstrumentationRegistry;
import android.util.Pair;

import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;


import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.RootMatchers.withDecorView;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static junit.framework.Assert.assertNotNull;
import static junit.framework.Assert.assertTrue;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.not;
import junit.framework.Assert.*;
import java.util.concurrent.CountDownLatch;
import com.udacity.gradle.builditbigger.MainActivity.EndpointsAsyncTask;
/**
 * Reference:
 *
 * Testing toast is defined and demonstrated by Bruno de Lima e Silva on Github
 * https://gist.github.com/brunodles/badaa6de2ad3a84138d517795f15efc7
 */

@RunWith(AndroidJUnit4.class)
public class MainActivityTest {

    @Rule
    public ActivityTestRule<MainActivity> mActivityRule = new ActivityTestRule<>(
            MainActivity.class);
/*
    @Test
    public void useAppContext() throws Exception {
        // Context of the app under test.
        Context appContext = InstrumentationRegistry.getTargetContext();

        assertEquals("com.udacity.gradle.builditbigger", appContext.getPackageName());
    } */

    @Test
    public void testBackendRetrieveJoke() {
        /*
         * 1. need a way to click the button
         * 2. need a way to capture text from toast
         * 3. verify text...
         */

        onView(withId(R.id.backend_button))
                .perform(click());

        onView(withText(R.string.joke_string)).inRoot(withDecorView(not(is(mActivityRule.getActivity().getWindow().getDecorView())))).check(matches(isDisplayed()));

    }

    @Test
    public void testVerifyJoke() throws InterruptedException {
        assertTrue(true);

        final CountDownLatch latch = new CountDownLatch(1);

        final Context context = mActivityRule.getActivity().getApplicationContext();
        EndpointsAsyncTask testTask = new EndpointsAsyncTask() {

            @Override
            protected void onPostExecute(String result) {

                assertNotNull(result);

                if (result != null)
                {
                    String expected = context.getResources().getString(R.string.joke_string);
                    assertEquals(expected, result);
                    latch.countDown();
                }
            }
        };

        String myName = context.getResources().getString( R.string.my_name );
        testTask.execute(new Pair<Context, String>(context, myName));
        latch.await();
    }
}
