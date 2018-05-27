package com.ctyeung.jokelib;

import java.util.Random;

/**
 * Created by ctyeung on 5/19/18.
 */

public class FrogJoke {

    private String[] jokes = {
            "When does a frog celebrates birthday ?\n\n\n...on leap year ",
            "What do we tell actors to break a leg ? \n\n\n... because every play has a cast ",
            "Hear about the new restaurant, Karma ? \n\n\n... there is no menu, you get what's deserved"
    };

    public String getJoke()
    {
        int index = 0;
        /*
         * Per suggestion, random number can be used but NOT when testing.
         * final int random = new Random().nextInt(3);
         */
        return jokes[index];
    }
}
