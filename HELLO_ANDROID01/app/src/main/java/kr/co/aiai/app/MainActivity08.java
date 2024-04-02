package kr.co.aiai.app;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity08 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main08);
        Log.d("juho","[MainActivity08]onCreate");
        Button btn = findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity08.this, MainActivity07.class);
                startActivity(intent);
            }
        });
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d("juho","[MainActivity08]onDestroy");;
    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.d("juho","[MainActivity08]onStart");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d("juho","[MainActivity08]onStop");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d("juho","[MainActivity08]onResume");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d("juho","[MainActivity08]onPause");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d("juho","[MainActivity08]onRestart");
    }
}