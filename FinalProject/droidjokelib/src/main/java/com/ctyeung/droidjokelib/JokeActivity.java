package com.ctyeung.droidjokelib;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.TextView;
import android.content.Intent;

public class JokeActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_joke);

        TextView textView = findViewById(R.id.jokeText);
        String jokeString = parseExtra();
        textView.setText(jokeString);
    }

    private String parseExtra()
    {
        String jokeString = this.getIntent().getStringExtra(Intent.EXTRA_TEXT);

        if(null==jokeString || 0==jokeString.length())
            jokeString = getResources().getString(R.string.null_joke);

        return jokeString;
    }
}
