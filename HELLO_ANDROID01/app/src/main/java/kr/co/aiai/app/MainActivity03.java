package kr.co.aiai.app;

import android.os.Bundle;
import android.text.Editable;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity03 extends AppCompatActivity {

    EditText et_dan, et_disp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main03);

        Button btn = findViewById(R.id.btn);
        et_dan = findViewById(R.id.et_dan);
        et_disp = findViewById(R.id.et_disp);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });
    }

    void myclick() {
        String dan = String.valueOf(et_dan.getText());
        int danNum = Integer.parseInt(dan);
        StringBuffer gugu = new StringBuffer();
        for (int i = 1; i <= 9; i++) {
            gugu.append(String.format("%d x %d = %d\n", danNum, i, (danNum * i)));
        }
        et_disp.setText(gugu);
    }
}