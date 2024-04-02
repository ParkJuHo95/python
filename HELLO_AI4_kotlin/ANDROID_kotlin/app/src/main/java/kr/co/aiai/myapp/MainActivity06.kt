package kr.co.aiai.myapp

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity

class MainActivity06 : AppCompatActivity() {

    lateinit var btn : Button
    lateinit var et_first : EditText
    lateinit var et_last : EditText
    lateinit var et_disp : EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main06)
        btn = findViewById(R.id.btn)
        et_first = findViewById(R.id.et_first)
        et_last = findViewById(R.id.et_last)
        et_disp = findViewById(R.id.et_disp)

        btn.setOnClickListener(){
            click()
        }
    }

    fun click(){
        var first:Int = Integer.valueOf(et_first.text.toString())
        var last:Int = Integer.valueOf(et_last.text.toString())

        var str:String = ""
        if(last-first>=0){
            for(i:Int in first..last){
                for(j:Int in 1..i){
                    str += "*"
                }
                str += "\n"
            }
        }else{
            for(i:Int in (last..first).reversed()){
                for(j:Int in 1..i){
                    str += "*"
                }
                str += "\n"
            }
        }
        et_disp.setText(str)
    }

//    fun getStar(cnt:Int):String{
//        var ret:String = ""
//        for(i:Int in 0..cnt){
//            ret += "*"
//        }
//        ret ="\n"
//        return ret
//    }
}