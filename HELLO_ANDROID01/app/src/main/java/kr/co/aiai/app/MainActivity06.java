package kr.co.aiai.app;

import android.os.Bundle;
import android.text.Editable;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.MultiAutoCompleteTextView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity06 extends AppCompatActivity {

    EditText et_first, et_last, et_disp;
    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main06);
        et_first = findViewById(R.id.et_first);
        et_last = findViewById(R.id.et_last);
        et_disp = findViewById(R.id.et_disp);
        btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                click();
            }
        });
    }

    void click(){
        int first = Integer.valueOf(String.valueOf(et_first.getText()));
        int last = Integer.valueOf(String.valueOf(et_last.getText()));

        String str = "";
        if(last-first >= 0) {
            for(int i=first; i<=last; i++) {
                for(int j=0;j<i;j++){
                    str += "*";
                }
                str+="\n";
            }
        } else {
            for(int i=first; i>=last; i--) {
                for(int j=0;j<i;j++){
                    str += "*";
                }
                str+="\n";
            }
        }
        et_disp.setText(str);
    }
}